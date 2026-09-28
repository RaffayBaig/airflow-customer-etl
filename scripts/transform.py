import pandas as pd

INPUT_FILE = "/opt/airflow/data/customers_raw.csv"
OUTPUT_FILE = "/opt/airflow/data/customers_clean.csv"


def transform():
    df = pd.read_csv(INPUT_FILE)

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Remove whitespace from text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Handle missing values
    df = df.fillna("Unknown")

    print("Transformation completed")
    print(df.head())

    df.to_csv(OUTPUT_FILE, index=False)

    return OUTPUT_FILE


if __name__ == "__main__":
    transform()