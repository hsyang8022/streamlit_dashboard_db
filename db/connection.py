import streamlit as st
from sqlalchemy import create_engine, text
# pymysql 보다 안정적임

@st.cache_resource
# 캐싱: 코드를 한번만 수행하고 캐시 메모리에 저장해서 이용하려고 하는거
# 한번 만들고 계속 재사용할 자원에 적합
# @st.cache_resource: 데이터에 변화가 없을때?? 사용
# @st.cache_data: 데이터 로딩 / 전처리 결과를 캐시메모리에 저장

# db 연결
def get_engine():
    db = st.secrets["mysql"] # secrets: 나한테만 가지고 있는 정보..  .streamlit: .(안보이게하는 기능)
    url = (
        f"mysql+pymysql://{db['user']}:{db['password']}"
        f"@{db['host']}:{db['port']}/{db['database']}"
        f"?charset={db['charset']}"
    )
    engine = create_engine(url, pool_pre_ping=True)
    return engine
# 연결정보에 쓰이는 기능 파라메터

# db 연결 테스트
def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return result.scalar()
# 연결이 잘되면 select 1 뜬다
# 1사용자가 db정보 유지할 수 있게끔 한다
# mysql에서 text() 이거 실행하게 함
# result는 실행 결과를 반환

# AWS RDS MySQL 연결(근데 내꺼는 안됨)
@st.cache_resource
def get_engine():
    engine = st.connection('weather_db', type='sql').engine
    return engine
