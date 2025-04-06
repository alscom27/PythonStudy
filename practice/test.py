# # 계속, 종료 메뉴
# def menu_se():
#     #     print("=" * 20)
#     #     print(
#     #         """1. 계속
#     # 2. 종료"""
#     #     )
#     #     print("=" * 20)
#     menu_se_str = f"{'='*20}\n1. 게속\n2.종료\n{'='*20}"
#     return menu_se_str


# # 커서(사용자가 메뉴 번호를 입력) 예외 처리
# # 메서드 안에 매개변수로 메서드가 가능
# def cursor_func(menu_func):
#     while True:
#         print(menu_func())
#         try:
#             cursor = int(input("메뉴 번호를 입력해주세요. "))
#         except ValueError:
#             print("잘 못 입력했습니다. 숫자를 입력해주세요.")
#             # 아래 방법은 계속 에러 발생 시 스택 오버플로우 가능성 있음.
#             # cursor_func()  # 숫자가 아닌 입력값을 받으면 재귀호출
#             continue
#         break
#     return cursor


# cursor_func(menu_se)


import re


# 계속, 종료 메뉴
def menu_se():
    print("=" * 20)
    print(
        """1. 계속
2. 종료"""
    )
    print("=" * 20)


def cursor_func(menu_func):
    while True:
        menu_func()
        # print(menu_func())
        try:
            cursor = int(input("메뉴 번호를 입력해주세요. "))
        except ValueError:
            print("잘 못 입력했습니다. 숫자를 입력해주세요.")
            # 아래 방법은 계속 에러 발생 시 스택 오버플로우 가능성 있음.
            # cursor_func()  # 숫자가 아닌 입력값을 받으면 재귀호출
            continue
        break
    return cursor


def menu_grade_mange():
    print("=" * 20)
    print(
        """1. 학생 성적 등록하기
2. 그만 등록하기"""
    )
    print("=" * 20)


############################################################

from konlpy.tag import Okt
from collections import defaultdict

text = "나는 사과를 먹고 학교에 갔다."

okt = Okt()
print(okt)
# <konlpy.tag._okt.Okt object at 0x000001E086EB2540>
tokens = okt.pos(text, stem=True)
print(tokens)
# [('나', 'Noun'), ('는', 'Josa'), ('사과', 'Noun'), ('를', 'Josa'), ('먹다', 'Verb'), ('학교', 'Noun'), ('에', 'Josa'), ('가다', 'Verb'), ('.', 'Punctuation')]

word_dict = defaultdict(int)
print(word_dict)
# defaultdict(<class 'int'>, {})
josa_dict = defaultdict(int)

for word, tag in tokens:
    if tag == "Josa":
        josa_dict[word] += 1
    elif tag in ["Noun", "Verb", "Adjective"]:
        word_dict[word] += 1

print("단어:", dict(word_dict))
print("조사:", dict(josa_dict))
# 단어: {'나': 1, '사과': 1, '먹다': 1, '학교': 1, '가다': 1}
# 조사: {'는': 1, '를': 1, '에': 1}
