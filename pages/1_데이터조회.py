# 조회한 결과를 보여주는 기능
import streamlit as st
import pandas as pd
from db.connection import get_engine
# 커넥션 파일에 있는 get_engine 함수를 쓰고 싶을 때
from db.crud import get_all_sales, search_sales
# db.crud 파일에 있는 get_all_sales 함수를 쓰고 싶을 때


st.title("🔎 판매데이터 조회")

with st.sidebar:
    st.header("조회 조건")
    category = st.text_input("카테고리")
    region = st.text_input("지역")
    keyword = st.text_input("상품명 키워드")

if st.button("조회"):
    df = search_sales(
        category=category if category else None,
        region=region if region else None,
        keyword=keyword if keyword else None
    )
else:
    df = get_all_sales()

st.dataframe(df, use_container_width=True)

# 해당 df를 data 폴더에 csv로 저장
csv = df.to_csv(index=False).encode("utf-8-sig") # 한글 깨짐 방지 위해 utf-8-sig로 인코딩
st.download_button(
    label="CSV 다운로드",
    data=csv,
    file_name="data/sales_data.csv",
    mime="text/csv"
)

