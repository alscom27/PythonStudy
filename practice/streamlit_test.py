# streamlit : 파이썬 개발자들이 데이터 시각화, 대시보드, 웹앱을 엄청 쉽게 만들 수 있게 해주는 툴
# 파이썬으로 GUI 웹앱을 쉽게 만드는 프레임워크

# pip install streamlit
# 실행은 터미널에서 streamlit run app.py 명령어
import streamlit as st

st.title("title")
st.header("header")
st.subheader("subheader")

# 공간을 2 : 3으로 분할
col1, col2 = st.columns([2, 3])

with col1:
    # col1에 담을 내용
    st.title("column1")

with col2:
    st.title("column2")
    st.checkbox("checkbox1")

# with구문 말고 다르게 사용
col1.subheader("column1 subheader")
col2.checkbox("checkbox2")

# streamlit 1.32버전 이상부터 link_button()으로 버튼에 링크를 달 수 있지만 무조건 새창에서 열림
# 현재 창에서 열리게하고 싶으면 markdown으로 html코드 써야가능
