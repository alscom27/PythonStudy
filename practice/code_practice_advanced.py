# gpt가 만들어준 문제

# 도전


# 계속, 종료 메뉴
def menu_se():
    print("=" * 20)
    print(
        """1. 계속
2. 종료"""
    )
    print("=" * 20)


# 커서(사용자가 메뉴 번호를 입력) 예외 처리
# 메서드 안에 매개변수로 메서드가 가능
def cursor_func(menu_func):
    while True:
        menu_func()
        try:
            cursor = int(input("메뉴 번호를 입력해주세요. "))
        except ValueError:
            print("잘 못 입력했습니다. 숫자를 입력해주세요.")
            continue
        break
    return cursor


# 1. 단어 빈도수 세기
# 입력된 문장에서 각 단어가 몇 번 나왔는지 딕셔너리로 정리
def word_frequency():
    while True:
        print("단어 빈도수 세기")

        cursor = cursor_func(menu_se)

        if cursor == 1:
            user_string = input("문장을 입력해주세요. ")

        elif cursor == 2:
            print("단어 빈도수 세기를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 2. json 파일에서 데이터 읽고 가공하기
# json 모듈 사용해서 데이터 불러오고, 필터링/출력

# 3. 날짜 차이 계산기
# datetime 모듈로 두 날짜 간 차이 구하기

# 4. 간단한 채팅 봇 만들기
# if-elif-else로 사용자의 입력에 반응하는 간단한 챗봇 만들기
