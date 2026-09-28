import pandas as pd

INPUT_FILE = "/opt/airflow/data/customers.csv"
OUTPUT_FILE = "/opt/airflow/data/customers_raw.csv"


def extract():
    df = pd.read_csv(INPUT_FILE)

    print(f"Extracted {len(df)} records")

    df.to_csv(OUTPUT_FILE, index=False)

    return OUTPUT_FILE


if __name__ == "__main__":
    extract()