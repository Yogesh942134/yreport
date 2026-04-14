import pytest
import pandas as pd
import numpy as np
import json
import os
import math
from yreport.health import data_health_report


def test_data_types_and_edge_cases():
    """Test various data types and edge cases like empty DF, all NaNs, etc."""
    # 1. Empty DataFrame (with columns)
    df_empty = pd.DataFrame(columns=["a", "b"])
    report = data_health_report(df_empty)
    # The current implementation returns NaN for empty dataframes because of .mean().mean() on empty
    assert math.isnan(report.health_score)
    assert report.shape["rows"] == 0

    # 2. DataFrame with all NaNs
    df_all_nan = pd.DataFrame({"a": [np.nan, np.nan], "b": [np.nan, np.nan]})
    report = data_health_report(df_all_nan)
    assert report.missing_percentage["a"] == 100.0
    assert report.health_score < 100.0

    # 3. Mixed types and special characters
    df_mixed = pd.DataFrame({
        "int": [1, 2, 3],
        "float": [1.1, 2.2, 3.3],
        "string": ["!@#", "$%^", "&*()"],
        "bool": [True, False, True],
        "date": pd.to_datetime(["2021-01-01", "2021-01-02", "2021-01-03"])
    })
    report = data_health_report(df_mixed)
    assert "int" in report.column_types["numeric"]
    assert "float" in report.column_types["numeric"]
    assert "string" in report.column_types["categorical"]
    assert "date" in report.column_types["datetime"]


def test_user_overrides():
    """Test categorical_cols, numeric_cols, and ignore_cols overrides."""
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "score": [10, 20, 30],
        "label": ["A", "B", "A"]
    })

    # Override 'id' to be categorical and ignore 'score'
    report = data_health_report(
        df,
        categorical_cols=["id"],
        ignore_cols=["score"]
    )

    assert "id" in report.column_types["categorical"]
    assert "score" not in report.column_types["numeric"]
    assert "score" not in report.column_types["categorical"]
    assert report.shape["columns"] == 2  # 'score' was dropped


def test_report_export_methods(tmp_path):
    """Test summary, to_dict, to_json, and to_markdown methods."""
    df = pd.DataFrame({
        "a": [1, 2, 3, 4, 1],
        "b": ["x", "y", "x", "y", "x"]
    })
    report = data_health_report(df)

    # 1. to_dict
    report_dict = report.to_dict()
    assert isinstance(report_dict, dict)
    assert report_dict["health_score"] == report.health_score

    # 2. to_json
    json_path = tmp_path / "report.json"
    report_json = report.to_json(path=str(json_path))
    assert os.path.exists(json_path)
    with open(json_path, "r") as f:
        loaded_json = json.load(f)
    assert loaded_json["health_score"] == report.health_score

    # 3. to_markdown
    md_path = tmp_path / "report.md"
    report_md = report.to_markdown(path=str(md_path))
    assert os.path.exists(md_path)
    assert "# Data Health Report" in report_md
    assert "## Summary" in report_md

    # 4. summary (ensure it runs without error)
    report.summary()


def test_numeric_diagnostics():
    """Test skewness and outlier detection."""
    # Skewed data with outliers
    # Corrected lengths: both arrays are 100 elements long
    df = pd.DataFrame({
        "normal": np.random.normal(0, 1, 100),
        "skewed": np.concatenate([np.random.exponential(1, 97), [100, 200, 300]])
    })
    report = data_health_report(df)

    assert "normal" in report.numeric
    assert "skewed" in report.numeric
    assert report.numeric["skewed"]["outlier_percentage"] > 0
    assert "log" in report.numeric["skewed"]["recommendation"].lower()


def test_recommendations_logic():
    """Test missing value recommendations and high cardinality."""
    # High missing values
    # Corrected lengths: all arrays are 100 elements long
    df = pd.DataFrame({
        "mostly_missing": [1] * 20 + [None] * 80,
        "some_missing": [1] * 80 + [None] * 20,
        "high_card": [str(i) for i in range(100)]
    })
    report = data_health_report(df)

    # Check missing recommendations
    missing_recs = report.recommendations["missing"]
    assert missing_recs["mostly_missing"]["action"] == "drop"
    assert missing_recs["some_missing"]["action"] == "impute"

    # Check cardinality warning
    assert "high_card" in report.warnings["high_cardinality"]


def test_input_validation():
    """Test that non-DataFrame input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        data_health_report([1, 2, 3])
