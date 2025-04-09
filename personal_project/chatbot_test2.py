# streamlit을 활용한 챗봇
import streamlit as st
from streamlit_chat import message
from konlpy.tag import Okt
import time
import requests
import random
import re

# pip install transformers sentencepiece torch
from transformers import pipeline


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
    "논란의 중심": [
        "백모씨",
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
    /*display : inline-block;*/
    max-width : 70%;
    word-wrap : break-word;
    display : flex;
    align-items : flex-start;
    overflow-wrap : break-word;
    height : auto;
    overflow : auto;
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

/*
.chat-input {
    position : fixed;
    bottom : 50px;
    left : 0;
    right : 0;
    background-color : #0e1117;
    padding : 10px;
    /* z-index : 100; */
}

.chat-input-textarea {
    margin : 0, 10px;
    width : 80%;
    min-height : 40px;
    resize : none;
}

.chat-input-wrapper {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #1e1e1e;
    padding: 10px;
    border-top: 1px solid #555;
    z-index: 100;
}

#chat-input {
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    font-size: 16px;
    resize: none;
    height: 50px;
    background-color: #2c2c2c;
    color: #fff;
    border: none;
    outline: none;
}
*/
</style>   
""",
        unsafe_allow_html=True,
    )


# 사이드바 대화내용 요약
def load_summarizer():
    return pipeline("summarization", model="digit82/kobart-summarization")


# 대화내용 요약
def summarize_conversation(messages, max_len=50):
    # 대화 요약 생성중 로딩?
    summarizer = load_summarizer()
    # 사용자/어시스턴트 내용을 전부 합친 뒤
    # full_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    full_text = "\n".join([f"{messages[1]["content"]}"])
    # full_text = "\n".join(
    #     [
    #         f"{messages[i]['role']}: {messages[i]['content']}"
    #         for i in range(1, len(messages) - 1)
    #     ]
    # )
    # 너무 길면 잘라주고
    full_text = full_text[:1024]  # 너무 길면 자르기

    prompt_text = (
        f"다음 대화 내용을 보고, 한 문장짜리 매우 짧은 한국어 제목을 만들어주세요. "
        f"실제 존재하는 단어만 사용하고, 의미 없는 조합은 피해주세요.\n\n"
        f"{full_text}"
    )
    # f"'{full_text}' 이 문장을 바탕으로 중복되지 않는 10자 이하의 제목을 만들어 주세요." 2
    # f"다음 대화를 보고 핵심 키워드로 짧은 제목 한 문장을 한국어로 만들어 주세요." 1
    # f"가능하다면 15자 이하로 해주세요. 대화 내용:\n{full_text}"1
    # max_length, min_length 조정
    summary = summarizer(full_text, max_length=15, min_length=10, do_sample=False)
    # 1차 결과에서 한 번 더 2차 요약을 진행하거나, 혹은 그냥 summary[0]["summary_text"]를 title로 써도 가능.
    # 만약 너무 길다면 다시 잘라주는 로직 추가해도 됨.
    # return summary[0]["summary_text"] # 수정 전

    raw_title = summary[0]["summary_text"]
    # 2차로 짧게 다듬어 달라고 프롬프트를 넣어 재요약(더 짧고 간결한 문장을 위해)
    second_prompt = f"'{raw_title}' 라는 문장을 15자 이하로 더 간결하게 줄여주세요."
    second_summary = summarizer(
        second_prompt, max_length=10, min_length=5, do_sample=False
    )

    # final_title = second_summary[0]["summary_text"]
    final_title = summary[0]["summary_text"]
    return final_title


# 말풍선 스타일 메세지 표시 함수
def display_chat_message(role, content, avatar_url):
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    message_class = "user-message" if role == "user" else "assistant-message"
    st.markdown(
        f"""<div class="chat-bubble {bubble_class} {message_class}">
                <img src="{avatar_url}" class="chat-avatar">
                <div>{content}</div>
                </div>
                """,
        unsafe_allow_html=True,
    )


# 로딩 화면에 표시
# def show_center_spinner():
#     st.markdown(
#         """
#         <div style='display:flex; justify-content:center; align-items:center; height:100px;'>
#             <div class="loader"></div>
#         </div>
#         <style>
#         .loader {
#           border: 8px solid #f3f3f3;
#           border-top: 8px solid #555;
#           border-radius: 50%;
#           width: 40px;
#           height: 40px;
#           animation: spin 1s linear infinite;
#         }

#         @keyframes spin {
#           0% { transform: rotate(0deg); }
#           100% { transform: rotate(360deg); }
#         }
#         </style>
#     """,
#         unsafe_allow_html=True,
#     )


# json 파싱 함수
def json_parsing():
    # 인증키
    service_key = "71efe28b43424ed79f88"
    # api 요청 주소
    url = f"http://openapi.foodsafetykorea.go.kr/api/{service_key}/COOKRCP01/json/1/100"
    # 요청 보내기
    response = requests.get(url)

    # 응답 확인
    if response.status_code == 200:
        data = response.json()

        items = data["COOKRCP01"]["row"]
    else:
        print("API 요청 실패 :", response.status_code)

    return items if response.status_code == 200 else response.status_code


# 단어가 한글자만 포함되도 매치 점수가 올라서 정확히 일차하면 카운트되게 수정
def word_in_text(word, text):
    return re.search(rf"\b{re.escape(word)}\b", text) is not None


# 대화 생성 함수
def generate_conversation(user_input):
    assistant_content = ""
    # 심심하니까 랜덤 문구들
    random_content = [
        "몇 가지 추천 레시피를 알려드릴게요. 😄\n",
        "추천 레시피를 알려드리겠습니다! 😎\n",
        "음...몇 가지 추천 요리들을 알려드릴게요. 🤔\n",
    ]
    # 매치 점수 저장 리스트
    scored_items = []

    # 사용자 대화내용 분석
    okt = Okt()
    tokens = okt.pos(user_input, stem=True)

    # 사용자 대화내용 키워드 분류
    nouns = [word for word, tag in tokens if tag == "Noun"]
    verbs = [word for word, tag in tokens if tag == "Verb"]

    # 형태소 분석기가 분석한 굽다와 json데이터의 굽기 가 매치 되지않아서 기를 다로 수정
    verb_methods = [verb[:1] + "기" for verb in verbs if verb.endswith("다")]

    # 데이터 가져오기
    items = json_parsing()
    # 데이터 돌면서 매치 점수 계산
    for item in items:
        score = 0
        name = item["RCP_NM"]
        ingredient = item["RCP_PARTS_DTLS"]
        method = item["RCP_WAY2"]

        # 음식명과 명사 키워드 일치시 매치점수 +1
        if any(word_in_text(noun, name) for noun in nouns):
            score += 1
        # 재료와 명사 일치시
        if any(word_in_text(noun, ingredient) for noun in nouns):
            score += 1
        # 조리방법과 동사 키워드 일치시
        if any(verb_method in method for verb_method in verb_methods):
            score += 1

        # 매치점수가 0보다 큰 것(언급된건) 전부 리스트로 등록
        if score > 0:
            scored_items.append((score, item))
    # 매치점수 높은 순으로 정렬
    # 키를 기준으로 내림차순
    scored_items.sort(key=lambda x: x[0], reverse=True)

    # 매치 점수 높은 5개 출력
    top_items = scored_items[:5]

    # 추천 레시피가 없으면
    if bool(top_items) == False:
        assistant_content = "추천드릴 레시피가 없습니다. 😢\n"
    # 추천 레시피가 있으면
    else:
        # randomint(x,y) x부터 y이하...
        assistant_content += (
            f"{random_content[random.randint(0,len(random_content)-1)]}"
        )
        for score, item in top_items:
            # 매치점수 : {score}\n
            assistant_content += f"""
✅ 매치 점수 : {score}\n
📋 요리명 : {item['RCP_NM']}\n
재료 : {item['RCP_PARTS_DTLS']}\n
조리법 : {item['RCP_WAY2']}\n
{'-'*20}\n

"""

    assistant_content += "\n💡 더 궁금하신게 있으면 물어봐주세요!"
    return assistant_content


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
    st.write("#### 💬 대화 목록")
    if st.button("➕ 새 대화"):
        st.session_state.stage = 1
        st.rerun()
        if st.session_state.chat_storage:
            # 사이드바 비율
            # 대화 목록 표시
            with st.spinner("요약 중..."):
                # summary = summarize_conversation(st.session_state.messages)
                # st.markdown(f"> {summary}")
                for i, chat in enumerate(st.session_state.chat_storage):
                    if st.button(chat["title"], key=f"load_chat_{i}"):
                        st.session_state.messages = chat["messages"].copy()
                        st.rerun()

#     if st.button("📝 지금까지 대화 요약하기"): 1
#         if st.session_state.messages:
#             with st.spinner("요약 중..."):
#                 summary = summarize_conversation(st.session_state.messages)
#                 st.success("요약 결과:")
#                 st.markdown(f"> {summary}")
#         else:
#             st.info("요약할 대화가 없습니다.")


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
        # st.markdown(
        #     '<div class="chat-input-wrapper"><textarea id="chat-input" class="chat-input-textarea" place-holder="대화를 입력하세요:">',
        #     unsafe_allow_html=True,
        # )
        user_input = st.chat_input("대화를 입력하세요:", key="input_conversation")
        st.markdown("</div>", unsafe_allow_html=True)
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.spinner("답변 생성 중...잠시만 기다려주세요."):
                # show_center_spinner()
                time.sleep(2)
            response = generate_conversation(user_input)
            st.session_state.messages.append({"role": "assistant", "content": response})
            title = summarize_conversation(st.session_state.messages)
            st.session_state.chat_storage.append(
                {"title": title, "messages": st.session_state.messages.copy()}
            )

            if st.session_state.chat_storage:
                # 사이드바 비율
                # 대화 목록 표시
                with st.sidebar:
                    with st.spinner("요약 중..."):
                        # summary = summarize_conversation(st.session_state.messages)
                        # st.markdown(f"> {summary}")
                        for i, chat in enumerate(st.session_state.chat_storage):
                            if st.button(chat["title"], key=f"load_chat_{i}"):
                                st.session_state.messages = chat["messages"].copy()
                                st.rerun()

            # if st.session_state.messages: 1
            #     with st.spinner("요약 중..."):
            #         summary = summarize_conversation(st.session_state.messages)
            #         # st.success("요약 결과:")
            #         st.markdown(f"> {summary}")
            # else:
            #     st.info("요약할 대화가 없습니다.")

    # 대화 히스토리 다시 표시
    chat_container.empty()  # 이전 메세지 지우기 ???
    with chat_container.container():
        if st.session_state.messages == False:
            # with st.spinner("답변 생성 중...잠시만 기다려주세요."):
            #     # show_center_spinner()
            #     time.sleep(3)
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
