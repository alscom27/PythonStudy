jsondata = [
    {
        "question": "리스트와 튜플의 가장 큰 차이점은 무엇인가요?",
        "answer": "리스트는 가변(mutable) 자료형으로, 요소의 추가, 삭제, 변경이 가능합니다. 반면, 튜플은 불변(immutable) 자료형으로, 한 번 생성된 후에는 요소의 변경이 불가능합니다.",
    },
    {
        "question": "언제 리스트를 사용하고 언제 튜플을 사용하는 것이 좋을까요?",
        "answer": "리스트: 데이터의 변경이 필요한 경우(예: 사용자 목록, 장바구니 품목), 튜플: 데이터의 변경이 필요하지 않은 경우(예: 좌표, 색상 코드, 설정 값) 또는 함수의 반환 값처럼 값이 고정되어야 하는 경우에 사용합니다. 튜플은 리스트보다 메모리 효율성이 높고 처리 속도가 빠릅니다.",
    },
    {
        "question": "리스트와 튜플의 요소에 접근하는 방법은 어떻게 다른가요?",
        "answer": "리스트와 튜플 모두 인덱싱(indexing)을 사용하여 요소에 접근합니다. 인덱스는 0부터 시작하며, 대괄호([]) 안에 인덱스 번호를 넣어 원하는 요소에 접근할 수 있습니다. 예를 들어, `my_list[0]` 또는 `my_tuple[0]`과 같이 사용합니다.",
    },
    {
        "question": "리스트에 요소를 추가하거나 삭제하는 방법은 무엇인가요?",
        "answer": "추가: `append()`, `insert()`, `extend()` 메서드를 사용하여 리스트에 요소를 추가할 수 있습니다. 삭제: `remove()`, `pop()`, `del` 키워드를 사용하여 리스트에서 요소를 삭제할 수 있습니다. 튜플은 요소의 추가 삭제가 불가능합니다.",
    },
    {
        "question": "리스트와 튜플의 슬라이싱(slicing)은 어떻게 사용하나요?",
        "answer": "슬라이싱은 리스트나 튜플에서 특정 범위의 요소를 추출하는 방법입니다. 콜론(:)을 사용하여 시작 인덱스와 끝 인덱스를 지정합니다. 예를 들어, `my_list[1:4]`는 인덱스 1부터 3까지의 요소를 추출합니다.",
    },
]


# print(jsondata)

# print("첫번째 질문 :", jsondata[0]["question"])

import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyD4IhzoCl1gP4sDJtEF7iRlr8lCaJLr6Oo")
model = genai.GenerativeModel("gemini-pro")

st.title(" Gemini API Demo")
user_input = st.text_input("메세지를 입력하세요.")ㄴ
