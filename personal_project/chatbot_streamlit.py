# streamlit을 활용한 챗봇
import streamlit as st
from streamlit_chat import message
from konlpy.tag import Okt

# 페이지 기본 설정
st.set_page_config(page_title="ChatBot", layout="wide")


# html 스타일
def chat_styles():
    st.markdown(
        """
<style>
.chat-bubble {
    padding : 10px;
    margin : 5px;
    border-radius : 10px;
    /* 텍스트 길이 맞춰 말풍선 길이 조정 */
    display : inline-block;
    max-width : 70%;
    word-wrap : break-word;
    display : flex;
    align-items : flex-start;
}

.user-bubble {
    background-color : gray;
    color : black;
    border-top-right-radius : 0;
    margin-left : auto;
    flex-dirction : row-reverse;
    gap : 10px;
}

.assistant-bubble {
    background-color : gray;
    color : black;
    border-top-left-radius : 0;
    margin-right : auto;
    gap : 10px;
}

.user-message {
    align-self : flex-end;
}

.assistant-message {
    align-self : flex-start;
}

</style>   
""",
        unsafe_allow_html=True,
    )


# 함수
def display_chat_message(role, content):
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    message_class = "user-message" if role == "user" else "assistant-message"
    st.markdown(
        f"""
                <div class="chat-bubble {bubble_class} {message_class}">
                <div>{content}</div>
                </div>
                """,
        unsafe_allow_html=True,
    )


chat_styles()


# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.character = None
    st.session_state.language = "한국어"
    # st.session_state.character_avatar_url = assistant_avatar_url
    st.session_state.stage = 1

# 대화 히스토리 표시
chat_container = st.empty()
with chat_container.container():
    st.markdown(
        '<div class="chat-wrapper"><div class="chat-container"', unsafe_allow_html=True
    )
    for msg in st.session_state.messages:
        # avatar 제외
        display_chat_message(msg["role"], msg["content"])
        st.markdown("</div></div>", unsafe_allow_html=True)

# 대화 처리 단계
# elif?
if st.session_state.stage == 1:
    user_input = st.chat_input("대화를 입력하세요:", key="input_conversation")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("답변 생성 중... 잠시만 기다려 주세요."):
            response = generate_conversation(
                st.session_state.language, st.session_state.character, user_input
            )
            st.session_state.messages.append({"role": "assistant", "content": response})

# 대화 히스토리 다시 표시
chat_container.empty()  # 이전 메세지 지우기
with chat_container.container():
    st.markdown(
        '<div class="chat-wrapper"><div class="chat-container">', unsafe_allow_html=True
    )
    for msg in st.session_state.messages:
        display_chat_message(msg["role"], msg["content"])
        st.markdown("</div></div>", unsafe_allow_html=True)
