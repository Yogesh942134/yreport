import pandas as pd
from yreport.health import data_health_report


def test_basic_data_health_report():
    df = pd.DataFrame({
        "age": [20, 21, None, 23],
        "salary": [10000, 15000, 20000, None],
        "city": ["A", "B", "B", "A"]
    })

    report = data_health_report(df)

    # Type & structure
    assert report is not None
    assert hasattr(report, "health_score")
    assert hasattr(report, "shape")
    assert hasattr(report, "column_types")

    # Core correctness
    assert report.shape["rows"] == 4
    assert report.shape["columns"] == 3

    # Missing detection
    assert report.missing_percentage["age"] == 25.0
    assert report.missing_percentage["salary"] == 25.0

    # Duplicate count
    assert report.duplicate_rows == 0

    # Column typing
    assert "city" in report.column_types["categorical"]
    assert "age" in report.column_types["numeric"]

    # Health score sanity
    assert 0 <= report.health_score <= 100
