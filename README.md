# dbt-intro: dbt with SQLite and Python Automation

A hands-on introduction to using **dbt (Data Build Tool)** with **SQLite**, featuring Python automation for seamless development and data validation.

## 🚀 Getting Started

Follow these steps to set up the environment and run the data pipeline.

### 1. Prerequisites
Ensure you have Python installed. Install the required dependencies:
```bash
pip install dbt-core dbt-sqlite pandas
```

### 2. Initialize Data
Run the setup script to create a fresh SQLite database (`data.db`) with raw sample data:
```bash
python setup_data.py
```

### 3. Run dbt & Automate
Execute the automation script to perform `dbt run` (deploy to SQLite), `dbt test`, and `dbt docs generate`:
```bash
python run_dbt_tasks.py
```

### 4. Verify & Query
Use the query script to inspect the generated models directly in SQLite:
```bash
python query_data.py
```

## 📂 Project Structure

- `models/`: dbt transformation logic (SQL).
  - `stg_customers.sql` & `stg_orders.sql`: Staging layers.
  - `customer_order_detail.sql`: Joined order details (Materialized as **Table**).
  - `customers_with_orders.sql`: Customer-level metrics.
- `setup_data.py`: Resets and initializes the database.
- `run_dbt_tasks.py`: Full dbt pipeline automation.
- `query_data.py`: Direct SQLite data inspection.
- `drop_dbt_model.py`: Utility to clean up generated models.
- `PROJECT_DOCS.md`: Detailed technical documentation.

## 🛠️ Key Features

- **Automated Deployment**: Custom Python logic in `run_dbt_tasks.py` automatically deploys compiled dbt models as tables into SQLite for client use.
- **Data Integrity**: Integrated dbt tests ensure uniqueness and non-null constraints on critical IDs.
- **Fresh Starts**: `setup_data.py` automatically clears existing data to prevent state pollution.

---
*Created as a learning project for dbt fundamentals.*
