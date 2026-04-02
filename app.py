import streamlit as st
from db.init_db import create_table_customer, seed_

st.set_page_config(
    page_title="Streamlit MySQL Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Streamlit + MySQL 대시보드")
st.write("멀티페이지 기반 CRUD 및 시각화 대시보드 예제입니다.")

st.info("""
왼쪽 사이드바에서 페이지를 선택하세요.

1. 데이터조회
2. 판매관리
3. 고객관리
4. 시각화
5. 대시보드
""")

create_table_customer()
seed_customer_data()