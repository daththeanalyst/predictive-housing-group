"""
Data Preparation Script — London House Price Prediction Benchmark
=================================================================
Reads raw data from the GeoSpatial Project and produces 2 clean CSVs:
  1. london_house_prices.csv  — property-level data (target: price)
  2. london_area_features.csv — outcode-level area features (crime, census, POIs)

Agents merge on the 'outcode' column.
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import glob
import os
import warnings
from sklearn.neighbors import BallTree

warnings.filterwarnings("ignore")

BASE = r"c:\Users\Dath\OneDrive\Desktop\AntiGravity Stuff\Done\GeoSpatial Project"
OUT = r"c:\Users\Dath\OneDrive\Desktop\AntiGravity Stuff\PREDICTIVE\agent-tooling-benchmark\data"

print("=" * 60)
print("LONDON HOUSE PRICE PREDICTION - DATA PREPARATION")
print("=" * 60)

# ============================================================
# STEP 1: Clean house prices
# ============================================================
print("\n[1/5] Loading house prices...")
hp = pd.read_csv(
    os.path.join(
        BASE,
        "House price data 2021 and Crime 2021",
        "kaggle_london_house_price_data (1).csv",
    )
)
print(f"  Raw: {hp.shape[0]:,} rows x {hp.shape[1]} cols")

# Keep columns for the benchmark
# Include rentEstimate so we can use it as a leakage bug in the broken pipeline
hp_clean = hp[
    [
        "outcode",
        "latitude",
        "longitude",
        "bedrooms",
        "bathrooms",
        "floorAreaSqM",
        "livingRooms",
        "propertyType",
        "tenure",
        "currentEnergyRating",
        "rentEstimate_currentPrice",
        "saleEstimate_currentPrice",
    ]
].copy()

hp_clean = hp_clean.rename(
    columns={
        "saleEstimate_currentPrice": "price",
        "currentEnergyRating": "energyRating",
        "rentEstimate_currentPrice": "rentEstimate",
    }
)

hp_clean = hp_clean.dropna(subset=["price", "latitude", "longitude", "outcode"])
print(f"  After dropping nulls in price/lat/lon/outcode: {hp_clean.shape[0]:,}")

# Compute outcode centroids for spatial matching
outcode_centroids = (
    hp_clean.groupby("outcode")
    .agg(
        outcode_lat=("latitude", "mean"),
        outcode_lon=("longitude", "mean"),
        n_properties=("price", "count"),
    )
    .reset_index()
)
print(f"  Unique outcodes: {outcode_centroids.shape[0]}")

# Build BallTree from outcode centroids (reused for all spatial matching)
centroids_rad = np.radians(outcode_centroids[["outcode_lat", "outcode_lon"]].values)
tree = BallTree(centroids_rad, metric="haversine")

# ============================================================
# STEP 2: Aggregate crime data to outcode level
# ============================================================
print("\n[2/5] Loading & aggregating crime data (12 months, Metropolitan Police)...")
crime_dir = os.path.join(BASE, "House price data 2021 and Crime 2021", "Crime data 2021")
met_files = sorted(glob.glob(os.path.join(crime_dir, "*", "*metropolitan-street.csv")))
print(f"  Found {len(met_files)} monthly files")

crimes_list = []
for f in met_files:
    df = pd.read_csv(f, usecols=["Latitude", "Longitude", "Crime type"])
    crimes_list.append(df)
crimes = pd.concat(crimes_list, ignore_index=True)
crimes = crimes.dropna(subset=["Latitude", "Longitude"])
print(f"  Total crime records with coordinates: {crimes.shape[0]:,}")

# Map each crime to nearest outcode
crime_rad = np.radians(crimes[["Latitude", "Longitude"]].values)
indices = tree.query(crime_rad, k=1, return_distance=False).flatten()
crimes["outcode"] = outcode_centroids.iloc[indices]["outcode"].values

# Pivot crime types to columns
crime_pivot = (
    crimes.groupby(["outcode", "Crime type"]).size().unstack(fill_value=0)
)
crime_pivot.columns = [
    "crime_" + c.lower().replace(" ", "_").replace("-", "_")
    for c in crime_pivot.columns
]
crime_pivot["crime_total"] = crime_pivot.sum(axis=1)
crime_pivot = crime_pivot.reset_index()
print(f"  Crime types: {crime_pivot.shape[1] - 2}")

# ============================================================
# STEP 3: Aggregate census to outcode level
# ============================================================
print("\n[3/5] Loading & aggregating census data...")
census_gdf = gpd.read_file(
    os.path.join(BASE, "data", "processed", "london_census_oa.geojson")
)
print(f"  Census Output Areas loaded: {census_gdf.shape[0]:,}")

# Convert to WGS84 and get centroids
census_gdf = census_gdf.to_crs(epsg=4326)
census_gdf["oa_lat"] = census_gdf.geometry.centroid.y
census_gdf["oa_lon"] = census_gdf.geometry.centroid.x

# Map each OA to nearest outcode
oa_rad = np.radians(census_gdf[["oa_lat", "oa_lon"]].values)
oa_indices = tree.query(oa_rad, k=1, return_distance=False).flatten()
census_gdf["outcode"] = outcode_centroids.iloc[oa_indices]["outcode"].values

# Identify numeric census columns
skip_cols = {
    "geometry",
    "geog_code",
    "geog_name",
    "oa_lat",
    "oa_lon",
    "outcode",
    "centroid_x",
    "centroid_y",
}
census_cols = [c for c in census_gdf.columns if c not in skip_cols]

# Convert to numeric and aggregate by outcode (mean)
census_numeric = census_gdf[["outcode"] + census_cols].copy()
for c in census_cols:
    census_numeric[c] = pd.to_numeric(census_numeric[c], errors="coerce")

census_agg = census_numeric.groupby("outcode")[census_cols].mean().reset_index()
census_agg.columns = ["outcode"] + ["census_" + c for c in census_cols]
print(f"  Census features: {len(census_cols)}")

# ============================================================
# STEP 4: Aggregate POIs to outcode level
# ============================================================
print("\n[4/5] Loading & aggregating POI data...")
pois = gpd.read_file(os.path.join(BASE, "data", "processed", "london_pois.geojson"))
pois = pois.to_crs(epsg=4326)
print(f"  POIs loaded: {pois.shape[0]:,}")

pois["poi_lat"] = pois.geometry.centroid.y
pois["poi_lon"] = pois.geometry.centroid.x
pois = pois.dropna(subset=["poi_lat", "poi_lon"])

# Map to nearest outcode
poi_rad = np.radians(pois[["poi_lat", "poi_lon"]].values)
poi_indices = tree.query(poi_rad, k=1, return_distance=False).flatten()
pois["outcode"] = outcode_centroids.iloc[poi_indices]["outcode"].values

# Find the type column
type_col = None
for candidate in ["amenity", "fclass", "type", "category"]:
    if candidate in pois.columns:
        type_col = candidate
        break

if type_col:
    poi_pivot = (
        pois.groupby(["outcode", type_col]).size().unstack(fill_value=0)
    )
    poi_pivot.columns = ["poi_" + str(c) for c in poi_pivot.columns]
else:
    poi_pivot = pois.groupby("outcode").size().to_frame("poi_total")

poi_pivot["poi_total"] = poi_pivot.sum(axis=1)
poi_pivot = poi_pivot.reset_index()
print(f"  POI categories: {poi_pivot.shape[1] - 2}")

# ============================================================
# STEP 5: Merge and save
# ============================================================
print("\n[5/5] Merging and saving...")

# Merge all area features
area = outcode_centroids.merge(crime_pivot, on="outcode", how="left")
area = area.merge(census_agg, on="outcode", how="left")
area = area.merge(poi_pivot, on="outcode", how="left")
area = area.fillna(0)

# Save
area.to_csv(os.path.join(OUT, "london_area_features.csv"), index=False)
hp_clean.to_csv(os.path.join(OUT, "london_house_prices.csv"), index=False)

print(f"\n  london_house_prices.csv: {hp_clean.shape[0]:,} rows x {hp_clean.shape[1]} cols")
print(f"  london_area_features.csv: {area.shape[0]} rows x {area.shape[1]} cols")

# Quick summary
print("\n" + "=" * 60)
print("DATA PREPARATION COMPLETE")
print("=" * 60)
print(f"\nHouse prices:")
print(f"  Rows: {hp_clean.shape[0]:,}")
print(f"  Missing bedrooms: {hp_clean['bedrooms'].isna().sum():,}")
print(f"  Missing bathrooms: {hp_clean['bathrooms'].isna().sum():,}")
print(f"  Missing floorAreaSqM: {hp_clean['floorAreaSqM'].isna().sum():,}")
print(f"  Missing energyRating: {hp_clean['energyRating'].isna().sum():,}")
print(f"  Missing rentEstimate: {hp_clean['rentEstimate'].isna().sum():,}")
print(f"  Price range: {hp_clean['price'].min():,.0f} - {hp_clean['price'].max():,.0f}")
print(f"  Median price: {hp_clean['price'].median():,.0f}")

print(f"\nArea features:")
print(f"  Outcodes: {area.shape[0]}")
print(f"  Features: {area.shape[1]}")
print(f"  Columns: {list(area.columns)}")
