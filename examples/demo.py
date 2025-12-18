import pandas as pd
from yreport import data_health_report

df = pd.read_csv("data/train.csv")

# Export Markdown
report  = data_health_report(df,ignore_cols=['Name','PassengerId'],categorical_cols=['Pclass'])


report.summary()

