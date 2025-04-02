str1 = "http://naver.com"

rule1 = str1[str1.rfind("/") + 1 :]
print(rule1)


str2 = "abad"
# str2_1 = str2.replace(str2[str2.rfind("a")], "c")
# 파이썬에서 단순 치환으로 2번지 a만은 바꿀 수 없음
print(str2[:2] + "cd")
# 가 그나마 가독성이 좋아보임.
