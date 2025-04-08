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

# 개체 설정
# 대화 보관함 (전체 목록) {대화 제목 : 대화내역}
if "chat_storage" not in st.session_state:
    st.session_state.chat_storage = {}

# 대화 목록의 대화들 , 대화내역 = [{"role" : "user", "content" : "대화내용"}, {"role" : "assistant", "content" : "응답내용"}]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 대화 내용, [{"role" : "user", "content" : "대화내용"}]
if "messages" not in st.session_state:
    st.session_state.messages = []

#

main_col1, main_col2 = st.columns([1, 9])

# 사이드바 비율
with st.sidebar:
    st.write("#### 대화 내용")
    if st.session_state.chat_storage:
        st.write("대화내용들 들어갈곳")

# 메인 뷰 비율
with main_col2:
    # 앱 제목
    st.title("🧠 챗봇")
    sub_head1, sub_head2, sub_head3 = st.columns([1, 1, 1])
    sub_col1, sub_col2, sub_col3 = st.columns([2, 2, 3])

    info_placeholder = st.empty()
    user_message = ""

    #
    with main_col2:
        if len(st.session_state.messages) == 0:
            with sub_head2:
                info_placeholder.markdown("#### 대화를 시작해보세요.")
                # assistant_info = st.write("#### 대화를 시작해보세요.")

        else:
            for msg in st.session_state.messages:
                display_chat_message(msg["role"], msg["content"])
                # with st.chat_message(msg["role"]):
                #     st.write(msg["content"])

with sub_col2:
    user_message = st.chat_input("대화를 입력해주세요. (500자 내외)")

    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
        # 채팅봇 로직
        st.session_state.messages.append({"role": "assistant", "content": "임시채팅"})
        # st.rerun()
