# streamlit을 활용한 챗봇
import streamlit as st
from streamlit_chat import message

# import google.generativeai as genai
from konlpy.tag import Okt

# 페이지 기본 설정
st.set_page_config(page_title="ChatBot", layout="wide")

# html 스타일
st.markdown(
    """
<style>
/* 채팅 입력폼 스타일 */
/*
.custom_chat_input input{
    border-radius : 10px;
    padding : 10px
    size : 100px 
}
*/

div[data_testId="stTextArea"]:nth-of-type(1) textarea{
    resize : none !important
}

</style>   
""",
    unsafe_allow_html=True,
)


# 함수
def display_chat_message(role, content, avartar_url):
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    message_class = "user-message" if role == "user" else "assistant-message"
    st.markdown(
        f"""
                <div class="chat-bubble {bubble_class} {message_class}">
                <img src="{avartar_url}" class="chat-avartar"></img>
                <div>{content}</div>
                </div>
                """,
        unsafe_allow_html=True,
    )


# 개체 설정
# 대화 보관함 (전체 목록) {대화 제목 : 대화내역}
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.charactor = None
    st.session_state.language = "한국어"
    st.session_state.charactor_avartar_url = assistant_avartar_url
    st.session_state.stage = 1
