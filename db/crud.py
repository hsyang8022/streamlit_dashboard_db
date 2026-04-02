# create, read, update, delete 기능 함수화

import streamlit as st
import pandas as pd
from sqlalchemy import text # text: sql문 불러오기
from db.connection import get_engine

######################################################################################################
# sale 테이블 CRUD
######################################################################################################


# sale 테이블 전체 조회하는 기능 : 매번 같은 테이블에서 조회할 때
# @st.cache_data(ttl = 300)
def get_all_sales():
    engine = get_engine()
    query = """
        SELECT id, order_date, product_name, category, quantity, price, region, created_at
        FROM sales
        ORDER BY id DESC
    """
    return pd.read_sql(query, engine)

# sale 테이블 조건 검색

def search_sales(category=None, region=None, keyword=None):
    engine = get_engine()

    conditions = []
    params = {}

    base_query = """
        SELECT id, order_date, product_name, category, quantity, price, region, created_at
        FROM sales
        WHERE 1=1
    """

    if category:
        conditions.append("AND category = :category")
        params["category"] = category

    if region:
        conditions.append("AND region = :region")
        params["region"] = region

    if keyword:
        conditions.append("AND product_name LIKE :keyword")
        params["keyword"] = f"%{keyword}%"

    final_query = base_query + "\n".join(conditions) + "\nORDER BY id DESC"

    return pd.read_sql(text(final_query), engine, params=params)

# sale id 로 검색 # 여기는 cache_data 붙일 이유가 없음 매번 달라지므로
def get_sale_by_id(sale_id):
    engine = get_engine()
    query = text("""
        SELECT id, order_date, product_name, category, quantity, price, region
        FROM sales
        WHERE id = :sale_id
    """)
    with engine.connect() as conn:
        result = conn.execute(query, {"sale_id": sale_id}).mappings().first()
        return dict(result) if result else None

# sale 데이터 삽입
def insert_sale(order_date, product_name, category, quantity, price, region):
    engine = get_engine()
    query = text("""
        INSERT INTO sales (order_date, product_name, category, quantity, price, region)
        VALUES (:order_date, :product_name, :category, :quantity, :price, :region)
    """)
    with engine.begin() as conn:
        conn.execute(query, {
            "order_date": order_date,
            "product_name": product_name,
            "category": category,
            "quantity": quantity,
            "price": price,
            "region": region
        })

# sale 데이터 갱신
def update_sale(sale_id, order_date, product_name, category, quantity, price, region):
    engine = get_engine()
    query = text("""
        UPDATE sales
        SET order_date = :order_date,
            product_name = :product_name,
            category = :category,
            quantity = :quantity,
            price = :price,
            region = :region
        WHERE id = :sale_id
    """)
    with engine.begin() as conn:
        conn.execute(query, {
            "sale_id": sale_id,
            "order_date": order_date,
            "product_name": product_name,
            "category": category,
            "quantity": quantity,
            "price": price,
            "region": region
        })

# sale 데이터 삭제(직접 정해야 하는 부분)

def delete_sale(sale_id):
    engine = get_engine()
    query = text("DELETE FROM sales WHERE id = :sale_id")
    with engine.begin() as conn:
        conn.execute(query, {"sale_id": sale_id})
