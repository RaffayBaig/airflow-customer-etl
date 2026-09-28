# Customer ETL Pipeline with Apache Airflow

An end-to-end ETL pipeline that extracts customer data from a CSV file, transforms it using Pandas, and loads the cleaned data into PostgreSQL. The workflow is orchestrated using Apache Airflow and runs inside Docker.

## Architecture

```text
customers.csv
     |
     v
  Extract
     |
     v
customers_raw.csv
     |
     v
 Transform
     |
     v
customers_clean.csv
     |
     v
   Load
     |
     v
 PostgreSQL
```

## Tech Stack

* Python
* Pandas
* Apache Airflow
* Docker
* PostgreSQL
* SQL
* Airflow PostgreSQLHook

## Project Structure

```text
AIRFLOW/
├── dags/
│   └── customer_etl_dag.py
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── data/
│   └── customers.csv
├── docker-compose.yaml
├── .env
├── .gitignore
└── README.md
```

## ETL Pipeline

### 1. Extract

The pipeline reads customer data from `customers.csv` and creates a raw data file.

### 2. Transform

The transformation step:

* Standardizes column names
* Removes unnecessary whitespace
* Handles missing values
* Produces a cleaned dataset

### 3. Load

The cleaned data is loaded into a PostgreSQL `customers` table using Airflow's PostgreSQL connection and hook.

The load operation uses an upsert strategy so that rerunning the pipeline does not create duplicate customer records.

## Airflow DAG

The pipeline is orchestrated using an Airflow DAG:

```text
Extract
   |
   v
Transform
   |
   v
Load
```

The DAG also demonstrates:

* Task dependencies
* Retries
* Docker-based Airflow execution
* Airflow Connections
* PostgreSQL hooks
* Idempotent loading

## PostgreSQL Table

The pipeline loads data into:

```sql
customers
```

with the following columns:

| Column  | Type    |
| ------- | ------- |
| id      | VARCHAR |
| name    | VARCHAR |
| segment | VARCHAR |
| state   | VARCHAR |
| city    | VARCHAR |

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AIRFLOW
```

### 2. Start Airflow

```bash
docker compose up -d
```

### 3. Open Airflow

Open:

```text
http://localhost:8080
```

### 4. Configure PostgreSQL

Create an Airflow PostgreSQL connection pointing to the target PostgreSQL database.

The connection credentials should be stored in Airflow rather than directly inside the Python code.

### 5. Trigger the DAG

Run:

```text
customer_etl_pipeline
```

The tasks execute in the following order:

```text
extract → transform → load
```

## Verification

After the DAG succeeds, verify the PostgreSQL table:

```sql
SELECT * FROM customers;
```

You can also check the number of loaded records:

```sql
SELECT COUNT(*) FROM customers;
```

## Key Concepts Demonstrated

* ETL pipelines
* Workflow orchestration
* Airflow DAGs
* Task dependencies
* Retries
* Airflow Connections
* PostgreSQL hooks
* Pandas transformations
* Docker
* PostgreSQL
* Idempotent data loading
