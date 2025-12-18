# yreport

yreport is a lightweight, dataset-agnostic data health reporting library
that provides actionable diagnostics for tabular datasets.

## Features
- Weighted data health score
- Missing value & cardinality diagnostics
- Honest categorical handling
- Numeric skewness & outlier detection
- User override support
- JSON & Markdown export

## Example
```python
from yreport import data_health_report

report = data_health_report(
    df,
    ignore_cols=["PassengerId"],
    categorical_cols=["Pclass"],
    drop_cols=None,
    numrical_cols=None
)

report.summary()
report.to_json("report.json")
report.to_markdown("report.md")
