import pandas as pd
from sqlalchemy import text
from db.connection import get_engine

def create_table_customer():
    engine = get_engine()

    create_sql = """
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        region VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        join_date DATE NOT NULL,
        sales DECIMAL(12,2) NOT NULL
    )
    """

    with engine.begin() as conn:
        conn.execute(text(create_sql))