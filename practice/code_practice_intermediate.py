# # gpt가 만들어준 문제

# 중급


# 계속, 종료 메뉴
def menu_se():
    print("=" * 20)
    print(
        """1. 계속
2. 종료"""
    )
    print("=" * 20)


# menu_se_str = f"{'='*20}\n1. 게속\n2.종료\n{'='*20}"
# return menu_se_str


# 커서(사용자가 메뉴 번호를 입력) 예외 처리
# 메서드 안에 매개변수로 메서드가 가능
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


# 1. 소수 판별기
# 입력한 숫자가 소수인지 아닌지 확인 (1과 자기 자신만 나눠지는 수)
def prime_discrimination():
    while True:
        print("소수(Prime) 판별기")

        # 메서드안에 매개변수로 메서드를 넣을 때 주의
        # ex. cursor_func(menu_se()) : 에러
        cursor = cursor_func(menu_se)

        if cursor == 1:
            while True:
                try:
                    user_num = int(input("판별할 숫자를 입력해주세요. "))
                except ValueError:
                    print("잘 못 입력했습니다. 숫자만 입력해주세요.")
                    continue
                break

            # 약수를 담을 리스트
            divisor_lsit = []
            for n in range(1, user_num + 1):
                if user_num % n == 0:
                    divisor_lsit.append(n)

            if len(divisor_lsit) == 2:
                print(f"""{divisor_lsit}로 {user_num}은(는) 소수(Prime)가 맞습니다.""")
                continue

            else:
                print(f"{user_num}은(는) 소수(Prime)가 아닙니다.")
                continue

        elif cursor == 2:
            print("소수(Prime) 판별기를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 2. 피보나치 수열 출력
# n번째까지 피보나치 수열 구하기 (0, 1, 1, 2, 3, 5, ...)

# 3. 계산기 만들기
# 두 수와 연산자(+, -, *, /)를 입력받아 계산 결과 출력
# + ^n 하면 거듭제곱도 되게 해보자


# 4. 숫자 야구 게임
# 3자리 숫자를 랜덤으로 만들고 ,사용자가 맞히는 게임
# 예: 123 vs 132 -> 1S 2B
# 이건 뭔 게임인지 몰라 찾아보자.

# 5. 학생 성적 관리 프로그램
# 여러 명의 이름과 점수를 입력받고, 평균/최고점/정렬 등을 출력


prime_discrimination()
