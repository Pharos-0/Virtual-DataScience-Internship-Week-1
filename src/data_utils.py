"""Helpers for loading the cleaned dataset with the correct data types.

CSV files do not store pandas dtypes, so the categorical columns are restored
here every time the cleaned file is read.
"""
import pandas as pd

from config import CLEAN_DATA_PATH

CONTRACT_ORDER = ["Month-to-month", "One year", "Two year"]

CATEGORICAL_COLUMNS = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "PhoneService",
    "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
    "Contract", "PaperlessBilling", "PaymentMethod", "Churn",
]
NUMERIC_COLUMNS = ["tenure", "MonthlyCharges", "TotalCharges"]


def load_clean_data(path=CLEAN_DATA_PATH):
    """Read the cleaned CSV and restore categorical dtypes."""
    df = pd.read_csv(path)
    for column in CATEGORICAL_COLUMNS:
        df[column] = df[column].astype("category")
    df["Contract"] = pd.Categorical(df["Contract"], categories=CONTRACT_ORDER, ordered=True)
    return df
