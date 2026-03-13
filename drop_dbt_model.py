import sqlite3
import os

def drop_dbt_models():
    # Define database path
    db_path = 'data.db'
    
    if not os.path.exists(db_path):
        print(f"Error: Database file '{db_path}' not found.")
        return

    # 1. Connect to SQLite database
    print(f"\nConnecting to database to drop dbt models...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Models to drop (they might be tables or views depending on dbt config)
    models = ['customer_order_detail', 'customers_with_orders', 'stg_customers', 'stg_orders']
    
    try:
        for model in models:
            print(f"Dropping model: {model}...")
            # Drop as view
            cursor.execute(f"DROP VIEW IF EXISTS {model};")
            # Drop as table (just in case)
            cursor.execute(f"DROP TABLE IF EXISTS {model};")
        
        conn.commit()
        print("Successfully dropped dbt models.")
        
    except Exception as e:
        print(f"An error occurred while dropping models: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    drop_dbt_models()
