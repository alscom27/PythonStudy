import re

text = "사과 딸기 수박 메론 바나나"
result = re.split(" ", text)
print(result)

text2 = """사과
딸기
수박
메론
바나나"""
result2 = re.split("\n", text2)
print(result2)
