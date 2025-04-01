# # 🔑 API 키 설정
# GOOGLE_API_KEY = (
#     "AIzaSyCvYSQEHx7_6h5s0RD1SFnSz1qri67F5HY"  # ← 여기에 본인의 API 키 입력
# )

import google.generativeai as genai
import json

# 설정: 본인 API 키 입력
genai.configure(api_key="AIzaSyCvYSQEHx7_6h5s0RD1SFnSz1qri67F5HY")

# ✅ 정확한 모델 이름: list_models에서 복사한 이름 그대로
model = genai.GenerativeModel("models/gemini-1.5-pro")

prompt = "리스트와 튜플 중요한거 5가지 씩 알려줘"

response = model.generate_content(prompt)

print(
    json.dumps(
        {"input": prompt, "output": response.text.strip()}, indent=4, ensure_ascii=False
    )
)


# import google.generativeai as genai

# genai.configure(api_key="AIzaSyCvYSQEHx7_6h5s0RD1SFnSz1qri67F5HY")

# models = genai.list_models()

# for m in models:
#     print(f"모델 이름: {m.name} | 지원 기능: {m.supported_generation_methods}")
