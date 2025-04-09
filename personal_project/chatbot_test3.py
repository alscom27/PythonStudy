# streamlit을 활용한 챗봇
import streamlit as st
from konlpy.tag import Okt
import time
import requests
import random
import re
from transformers import pipeline

# 페이지 기본 설정
st.set_page_config(page_title="ChatBot", layout="wide")

# 캐릭터 이미지
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

user_avatar_url = "https://png.pngtree.com/png-vector/20191009/ourmid/pngtree-user-icon-png-image_1796659.jpg"
assistant_avatar_url = (
    "https://img.freepik.com/free-vector/chatbot-chat-message-vectorart_78370-4104.jpg"
)

# HTML 스타일
st.markdown(
    """<style>.chat-bubble{padding:10px;margin:5px;border-radius:10px;max-width:70%;word-wrap:break-word;display:flex;align-items:flex-start;overflow-wrap:break-word;}.chat-avatar{width:50px;height:50px;border-radius:50%;margin-right:10px;object-fit:cover;}.user-bubble{background-color:gray;color:black;border-top-right-radius:0;margin-left:auto;flex-direction:row-reverse;gap:10px;}.assistant-bubble{background-color:gray;color:black;border-top-left-radius:0;margin-right:auto;gap:10px;}.user-message{align-self:flex-end;}.assistant-message{align-self:flex-start;}</style>""",
    unsafe_allow_html=True,
)


# 요약기 불러오기
def load_summarizer():
    return pipeline("summarization", model="digit82/kobart-summarization")


def summarize_conversation(messages):
    summarizer = load_summarizer()
    full_text = "\n".join([f"{m['role']}: {m['content']}" for m in messages])[:1024]
    prompt = f"다음 대화 내용을 보고, 한 문장짜리 매우 짧은 한국어 제목을 만들어주세요.\n\n{full_text}"
    summary = summarizer(prompt, max_length=15, min_length=10, do_sample=False)
    return summary[0]["summary_text"]


def display_chat_message(role, content, avatar_url):
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    message_class = "user-message" if role == "user" else "assistant-message"
    st.markdown(
        f"""<div class="chat-bubble {bubble_class} {message_class}"><img src="{avatar_url}" class="chat-avatar"><div>{content}</div></div>""",
        unsafe_allow_html=True,
    )


def json_parsing():
    service_key = "71efe28b43424ed79f88"
    url = f"http://openapi.foodsafetykorea.go.kr/api/{service_key}/COOKRCP01/json/1/100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["COOKRCP01"]["row"]
    return []


def word_in_text(word, text):
    return re.search(rf"\\b{re.escape(word)}\\b", text) is not None


def generate_conversation(user_input):
    assistant_content = ""
    random_content = [
        "몇 가지 추천 레시피를 알려드릴게요. 😄\n",
        "추천 레시피를 알려드리겠습니다! 😎\n",
        "음...몇 가지 추천 요리들을 알려드릴게요. 🤔\n",
    ]
    scored_items = []
    okt = Okt()
    tokens = okt.pos(user_input, stem=True)
    nouns = [word for word, tag in tokens if tag == "Noun"]
    verbs = [
        word[:1] + "기" for word, tag in tokens if tag == "Verb" and word.endswith("다")
    ]
    items = json_parsing()
    for item in items:
        score = 0
        if any(word_in_text(noun, item["RCP_NM"]) for noun in nouns):
            score += 1
        if any(word_in_text(noun, item["RCP_PARTS_DTLS"]) for noun in nouns):
            score += 1
        if any(verb in item["RCP_WAY2"] for verb in verbs):
            score += 1
        if score > 0:
            scored_items.append((score, item))
    scored_items.sort(key=lambda x: x[0], reverse=True)
    top_items = scored_items[:5]
    if not top_items:
        assistant_content = "추천드릴 레시피가 없습니다. 😢\n"
    else:
        assistant_content += random.choice(random_content)
        for score, item in top_items:
            assistant_content += f"✅ 매치 점수 : {score}\n📋 요리명 : {item['RCP_NM']}\n재료 : {item['RCP_PARTS_DTLS']}\n조리법 : {item['RCP_WAY2']}\n{'-'*20}\n"
    assistant_content += "\n💡 더 궁금하신게 있으면 물어봐주세요!"
    return assistant_content


st.title("🧠 챗봇")

if "chat_storage" not in st.session_state:
    st.session_state.chat_storage = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "character" not in st.session_state:
    st.session_state.character = None
if "character_avatar_url" not in st.session_state:
    st.session_state.character_avatar_url = assistant_avatar_url

with st.sidebar:
    st.write("#### 💬 대화 목록")
    if st.button("➕ 새 대화"):
        st.session_state.messages = []
        st.session_state.stage = 1
        st.rerun()
    for i, chat in enumerate(st.session_state.chat_storage):
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(chat["title"], key=f"load_chat_{i}"):
                st.session_state.messages = chat["messages"].copy()
                st.session_state.stage = 2
                st.rerun()
        with col2:
            if st.button("🗑", key=f"delete_chat_{i}"):
                del st.session_state.chat_storage[i]
                st.rerun()

if st.session_state.stage == 1:
    st.markdown("<h3>캐릭터를 선택하세요:</h3>", unsafe_allow_html=True)
    for character, info in characters.items():
        if st.button(f"{character} 선택"):
            st.session_state.character = character
            st.session_state.character_avatar_url = info[1]
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": f"안녕하세요! {character}입니다. 무엇을 도와드릴까요?",
                }
            )
            st.session_state.stage = 2
            st.rerun()

elif st.session_state.stage == 2:
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
    user_input = st.chat_input("대화를 입력하세요:")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("답변 생성 중..."):
            time.sleep(2)
            response = generate_conversation(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        title = summarize_conversation(st.session_state.messages)
        st.session_state.chat_storage.append(
            {"title": title, "messages": st.session_state.messages.copy()}
        )
        st.rerun()

###########################
# 대화 목록 누르면 채팅기록은 가져오는데 아바타 못갖고 오는거 수정
# 데이터 매칭 안되서 출력되는거 수정
# 캐릭터 선택 이미지 안보이는거 수정
# 제목 요약 이상하게 되는건 어쩔 수 없는 듯...
# + 유저 인풋 먼저 보이고 답변생성중 로딩 보이기
# 채팅창 하단 붙는거 굳
