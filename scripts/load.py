import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

INPUT_FILE = "/opt/airflow/data/customers_clean.csv"

def load():
    df = pd.read_csv(INPUT_FILE)

    hook = PostgresHook(
        postgres_conn_id="customer_postgres"
    )

    rows = [
        (
            row["id"],
            row["name"],
            row["segment"],
            row["state"],
            row["city"],
        )
        for _, row in df.iterrows()
    ]

    connection = hook.get_conn()
    cursor = connection.cursor()

    cursor.executemany(
        """
        INSERT INTO customers
        (id, name, segment, state, city)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id)
        DO UPDATE SET
            name = EXCLUDED.name,
            segment = EXCLUDED.segment,
            state = EXCLUDED.state,
            city = EXCLUDED.city;
        """,
        rows
    )

    connection.commit()

    cursor.close()
    connection.close()

    print(f"Loaded {len(rows)} records into PostgreSQL.")


if __name__ == "__main__":
    load()