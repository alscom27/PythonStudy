# # 🔑 API 키 설정
# GOOGLE_API_KEY = (
#     "AIzaSyCvYSQEHx7_6h5s0RD1SFnSz1qri67F5HY"  # ← 여기에 본인의 API 키 입력
# )

# genai 임포트 위해서 pip install google-generativeai 를 설치
# 어떤환경에서 설치했는지 확인해야함 설치한 환경에서 실행
import google.generativeai as genai
import json

# 설정: 본인 API 키 입력
genai.configure(api_key="AIzaSyCvYSQEHx7_6h5s0RD1SFnSz1qri67F5HY")

# genai.GenerativeModel(): ()에는 list_models에서 복사한 이름 그대로 사용할 모델을 입력
model = genai.GenerativeModel("models/gemini-1.5-pro")

# 질문
prompt = "리스트와 튜플 중요한거 5가지 씩 알려줘"
# 응답
response = model.generate_content(prompt)

# 질문과 답변을 json (튜플안에 딕셔너리) 형태로 출력
print(
    json.dumps(
        {"input": prompt, "output": response.text.strip()}, indent=4, ensure_ascii=False
    )
)

# 발급받은 gemini api 키로 어떤 모델을 쓸 수있는지 목록 출력
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyCvYSQEHx7_6h5s0RD1SFnSz1qri67F5HY")

# models = genai.list_models()

# for m in models:
#     print(f"모델 이름: {m.name} | 지원 기능: {m.supported_generation_methods}")
