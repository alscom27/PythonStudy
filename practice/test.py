# 계속, 종료 메뉴
def menu_se():
    #     print("=" * 20)
    #     print(
    #         """1. 계속
    # 2. 종료"""
    #     )
    #     print("=" * 20)
    menu_se_str = f"{'='*20}\n1. 게속\n2.종료\n{'='*20}"
    return menu_se_str


# 커서(사용자가 메뉴 번호를 입력) 예외 처리
# 메서드 안에 매개변수로 메서드가 가능
def cursor_func(menu_func):
    while True:
        print(menu_func())
        try:
            cursor = int(input("메뉴 번호를 입력해주세요. "))
        except ValueError:
            print("잘 못 입력했습니다. 숫자를 입력해주세요.")
            # 아래 방법은 계속 에러 발생 시 스택 오버플로우 가능성 있음.
            # cursor_func()  # 숫자가 아닌 입력값을 받으면 재귀호출
            continue
        break
    return cursor


cursor_func(menu_se)
