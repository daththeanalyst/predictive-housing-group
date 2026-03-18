
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


REQUIRED_FEATURES = [
    'bedrooms',
    'bathrooms',
    'floorAreaSqM',
    'livingRooms',
    'crime_total',
    'census_denom_total',
]


def load_inputs(prices_path, areas_path):
    prices = pd.read_csv(prices_path)
    areas = pd.read_csv(areas_path)
    return prices, areas


def validate_inputs(prices, areas):
    required_price_cols = {'outcode', 'price'}
    required_area_cols = {'outcode', 'crime_total', 'census_denom_total'}

    missing_price = sorted(required_price_cols - set(prices.columns))
    missing_area = sorted(required_area_cols - set(areas.columns))
    if missing_price:
        raise KeyError(f"Missing required columns in prices: {missing_price}")
    if missing_area:
        raise KeyError(f"Missing required columns in areas: {missing_area}")

    dup_outcode_count = int(areas['outcode'].duplicated().sum())
    if dup_outcode_count > 0:
        raise ValueError(f"Area table contains {dup_outcode_count} duplicate outcode rows.")


def merge_with_validation(prices, areas):
    return prices.merge(areas, on='outcode', how='left', validate='m:1')


def select_features_target(df):
    missing = sorted((set(REQUIRED_FEATURES) | {'price'}) - set(df.columns))
    if missing:
        raise KeyError(f"Missing required columns after merge: {missing}")
    x = df[REQUIRED_FEATURES].copy()
    y = df['price'].copy()
    if (y <= 0).any():
        raise ValueError("Target contains non-positive values.")
    return x, y


def split_data(x, y, random_state=42, test_size=0.2):
    return train_test_split(x, y, test_size=test_size, random_state=random_state)


def build_pipeline(random_state=42):
    numeric_preprocess = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
    ])
    preprocess = ColumnTransformer(
        transformers=[('num', numeric_preprocess, REQUIRED_FEATURES)],
        remainder='drop',
    )
    model = RandomForestRegressor(
        n_estimators=300,
        random_state=random_state,
        n_jobs=-1,
    )
    return Pipeline(steps=[('preprocess', preprocess), ('model', model)])


def compute_metrics(y_true, y_pred):
    return {
        'RMSE': float(np.sqrt(mean_squared_error(y_true, y_pred))),
        'MAE': float(mean_absolute_error(y_true, y_pred)),
        'R2': float(r2_score(y_true, y_pred)),
    }


def run_corrected_pipeline(prices_path, areas_path, random_state=42, test_size=0.2):
    prices, areas = load_inputs(prices_path, areas_path)
    validate_inputs(prices, areas)
    df = merge_with_validation(prices, areas)
    x, y = select_features_target(df)
    x_train, x_test, y_train, y_test = split_data(x, y, random_state=random_state, test_size=test_size)

    pipe = build_pipeline(random_state=random_state)
    pipe.fit(x_train, y_train)
    y_pred = pipe.predict(x_test)

    metrics = compute_metrics(y_test, y_pred)
    diagnostics = pd.DataFrame({
        'actual': y_test.reset_index(drop=True),
        'predicted': pd.Series(y_pred),
    })
    diagnostics['residual'] = diagnostics['actual'] - diagnostics['predicted']
    diagnostics['abs_error'] = diagnostics['residual'].abs()

    return {
        'pipeline': pipe,
        'metrics': metrics,
        'x_test': x_test,
        'y_test': y_test,
        'predictions': y_pred,
        'diagnostics': diagnostics,
    }
