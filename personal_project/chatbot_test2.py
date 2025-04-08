# streamlit을 활용한 챗봇
import streamlit as st
from streamlit_chat import message
from konlpy.tag import Okt
import time

# 페이지 기본 설정
st.set_page_config(page_title="ChatBot", layout="wide")

# streamlit에 있는 st.chat_message 사용하려다가 도저히 공간 분리가 안되서 결국 markdown으로 내가줌...
# 캐릭터 이미지(유저가 사용할 이미지)
characters = {
    "3스타 쉐프": [
        "안성재",
        "https://img.khan.co.kr/news/2024/10/23/l_2024102301000679900063701.jpg",
    ],
    "불안핑": [
        "윤남노",
        "https://i.namu.wiki/i/YEr_K9uN-yXUwvjjTwPKZRnJeSQAcJ01il5Byjt0nbLF49EoYFTpWlZMOBdNmD6ucIp0wyvoLVLe5bt5eFwjwg.webp",
    ],
    "화제의 중심": [
        "백종원",
        "https://dimg.donga.com/wps/NEWS/IMAGE/2024/10/17/130239330.2.png",
    ],
}

# 사용자 아바타 이미지 url
user_avatar_url = "https://png.pngtree.com/png-vector/20191009/ourmid/pngtree-user-icon-png-image_1796659.jpg"
assistant_avatar_url = (
    "https://img.freepik.com/free-vector/chatbot-chat-message-vectorart_78370-4104.jpg"
)


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

.chat-avatar {
    width: 50px;
    height : 50px;
    border-radius : 50%;
    margin-right : 10px;
    object-fit : cover;
}

.user-bubble {
    background-color : gray;
    color : black;
    border-top-right-radius : 0;
    margin-left : auto;
    flex-direction : row-reverse;
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

.spinner-container {
    display : flex;
    justify-content : center;
    align-items : center;
    margin : 10px 0;
}

.member-card {
    /* background-color: #f1f1f1; */
    border : none;
    padding : 10px;
    margin : 5px;
    border-radius:10px;
    display : flex;
    flex-direction : column;
    align-items:center;
    cursor : pointer;
    width : 200px;
    /* text-align : center; */
}

.member-card img {
    border-radius : 50%;
    width : 100px;
    height : 100px;
    object-fit: cover;
    margin-bottom: 10px;
    margin-right : 80px;
}

.member-card span {
    margin-bottom: 10px;
    margin-right : 80px;
}

.member-button {
    background-color: #4CAF50;
    color : white;
    border : none;
    padding : 30px;
    text-align : center;
    text-decoration : none;
    display : inline-block;
    font-size : 14px;
    cursor : pointer;
    border-radius : 5px;
    width: 100%
    box-sizing : border-box;
    margin-left : 80px;
}

.member-card button {
    background-color : transparent;
    border : none;
    padding:0;
    text-align : center;
    cursor : pointer;
    margin-left : 80px;
}

</style>   
""",
        unsafe_allow_html=True,
    )


# 말풍선 스타일 메세지 표시 함수
def display_chat_message(role, content, avatar_url):
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    message_class = "user-message" if role == "user" else "assistant-message"
    st.markdown(
        f"""
                <div class="chat-bubble {bubble_class} {message_class}">
                <img src="{avatar_url}" class="chat-avatar">
                <div>{content}</div>
                </div>
                """,
        unsafe_allow_html=True,
    )


def show_center_spinner():
    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; height:100px;'>
            <div class="loader"></div>
        </div>
        <style>
        .loader {
          border: 8px solid #f3f3f3;
          border-top: 8px solid #555;
          border-radius: 50%;
          width: 40px;
          height: 40px;
          animation: spin 1s linear infinite;
        }

        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


# 대화 생성 함수
def generate_conversation():
    pass


st.title("🧠 챗봇")

chat_styles()


# 개체 설정 세션 상태 초기화
# 대화 보관함 (전체 목록) [{대화 제목 : messages[]}]
if "chat_storage" not in st.session_state:
    st.session_state.chat_storage = []
# 대화 목록의 대화들 , 대화내역 = [{"role" : "user", "content" : "대화내용"}, {"role" : "assistant", "content" : "응답내용"}]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# 대화 내용, [{"role" : "user", "content" : "대화내용"}]
if "messages" not in st.session_state:
    st.session_state.messages = []
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "character" not in st.session_state:
    st.session_state.character = None
if "character_avatar_url" not in st.session_state:
    st.session_state.character_avatar_url = assistant_avatar_url


main_col1, main_col2 = st.columns([1, 9])

# 사이드바 비율
# 대화 목록 표시
with st.sidebar:
    st.write("#### 대화 내용")
    if st.session_state.chat_storage:
        st.write("대화내용들 들어갈곳")

# 메인 뷰 비율
with main_col2:
    # 앱 제목
    # st.title("🧠 챗봇")

    # 대화 히스토리 표시
    sub_head1, sub_head2, sub_head3 = st.columns([1, 3, 1])
    sub_col1, sub_col2, sub_col3 = st.columns([2, 2, 3])

    chat_container = st.empty()
    with sub_head2:
        with chat_container.container():
            st.markdown(
                '<div class="chat-wrapper"><div class="chat-container">',
                unsafe_allow_html=True,
            )
            for msg in st.session_state.messages:
                display_chat_message(
                    msg["role"],
                    msg["content"],
                    (
                        st.session_state.character_avatar_url
                        if msg["role"] == "assistant"
                        else user_avatar_url
                    ),
                )
                st.markdown("</div></div>", unsafe_allow_html=True)

    # 챗봇 캐릭터 선택 단계
    if st.session_state.stage == 1:
        selected_character = None
        st.markdown('<div class="member-selection">', unsafe_allow_html=True)
        st.markdown("<h3>캐릭터를 선택하세요:</h3>", unsafe_allow_html=True)
        for character, info in characters.items():  # 키 : 값
            character_key = f"button_{character}"
            # <span>{character}</span>
            st.markdown(
                f"""<div class="member-card" id="{character_key}">
                        <img src="{info[1]}" class="chat-avatar">
                        <span>{character}</span>
                        </div>""",
                unsafe_allow_html=True,
            )
            if st.button(f"{character} 선택", key=f"{character_key}_button"):
                selected_character = character
                break

        if selected_character:
            st.session_state.character = selected_character
            st.session_state.character_avatar_url = characters[selected_character][1]
            request_message = (
                f"안녕하세요! {selected_character}입니다. 무엇을 도와드릴까요?"
            )
            st.session_state.messages.append(
                {"role": "assistant", "content": request_message}
            )
            st.session_state.stage = 2
            st.rerun()

    # 대화 처리 단계
    elif st.session_state.stage == 2:
        user_input = st.chat_input("대화를 입력하세요:", key="input_conversation")
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            # with st.spinner("답변 생성 중...잠시만 기다려주세요."):
            #     show_center_spinner()
            #     time.sleep(10)
            response = generate_conversation()
            st.session_state.messages.append({"role": "assistant", "content": response})

    # 대화 히스토리 다시 표시
    chat_container.empty()  # 이전 메세지 지우기 ???
    with chat_container.container():
        if st.session_state.messages == False:
            with st.spinner("답변 생성 중...잠시만 기다려주세요."):
                # show_center_spinner()
                time.sleep(3)
        st.markdown(
            '<div class="chat-wrapper"><div class="chat-container">',
            unsafe_allow_html=True,
        )
        for msg in st.session_state.messages:
            display_chat_message(
                msg["role"],
                msg["content"],
                (
                    st.session_state.character_avatar_url
                    if msg["role"] == "assistant"
                    else user_avatar_url
                ),
            )
            st.markdown("</div></div>", unsafe_allow_html=True)
