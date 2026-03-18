
import pandas as pd
import debug_pipeline


def test_required_features_present():
    assert isinstance(debug_pipeline.REQUIRED_FEATURES, list)
    assert 'bedrooms' in debug_pipeline.REQUIRED_FEATURES


def test_validate_inputs_passes_for_current_data():
    prices = pd.read_csv('london_house_prices.csv')
    areas = pd.read_csv('london_area_features.csv')
    debug_pipeline.validate_inputs(prices, areas)


def test_run_corrected_pipeline_returns_metrics():
    out = debug_pipeline.run_corrected_pipeline('london_house_prices.csv', 'london_area_features.csv', random_state=42)
    metrics = out['metrics']
    assert set(metrics.keys()) == {'RMSE', 'MAE', 'R2'}
    assert metrics['RMSE'] > 0
