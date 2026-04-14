def test_yreport_inspector_pipeline():
    import pandas as pd
    from sklearn.compose import ColumnTransformer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder

    from yreport import YReportInspector

    # Dummy dataset
    x = pd.DataFrame({"num": [1, 2, 3, 4], "cat": ["a", "b", "a", "b"]})
    y = [0, 1, 0, 1]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(), ["cat"]),
            ("num", "passthrough", ["num"]),
        ]
    )

    pipe = Pipeline(
        [
            ("inspect", YReportInspector(categorical_cols=["cat"])),
            ("preprocessor", preprocessor),
            ("model", LogisticRegression()),
        ]
    )

    # Should fit without error
    pipe.fit(x, y)

    # Inspector must store report_
    inspector = pipe.named_steps["inspect"]
    assert hasattr(inspector, "report_")

    # Model must still predict
    preds = pipe.predict(x)
    assert len(preds) == len(x)
