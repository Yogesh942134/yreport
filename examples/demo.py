# import pandas as pd
# from yreport import data_health_report
#
# df = pd.read_csv("data/train.csv")
#
# # Export Markdown
# report  = data_health_report(df,ignore_cols=['Name','PassengerId'],categorical_cols=['Pclass'])
#
#
# report.summary()


import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from yreport.sklearn import YReportInspector
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("data/train.csv",usecols=["Age","Fare","Survived"])

X = df.drop("Survived",axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ("inspect", YReportInspector()),
    ('impute',SimpleImputer(strategy="median")),
    ("model", LogisticRegression())
])

pipe.fit(X_train, y_train)

pipe.named_steps["inspect"].report_.summary()
