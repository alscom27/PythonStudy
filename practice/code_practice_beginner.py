# gpt가 만들어준 문제

# 초급


def sel_menu_se():
    print("=" * 20)
    print(
        """1. 계속
2. 종료"""
    )
    print("=" * 20)
    print("메뉴 번호를 입력해주세요. ", end="")


# 1. 홀짝 판별기
# 사용자에게 숫자를 입력받아, 홀수인지 짝수인지 출력하자


def odd_even_disc():
    while True:
        print("홀짝 판별기")
        try:
            input_num = int(input("판별하고 싶은 숫자를 입력하세요. "))

            if input_num % 2 == 0:
                print("짝수 입니다.")

                sel_menu_se()
                cursor = int(input())

                if cursor == 1:
                    print("계속하기")
                    continue
                elif cursor == 2:
                    print("홀짝 판별기를 종료합니다.")
                    break
                else:
                    print("잘못된 입력입니다. 홀짝 판별기를 종료합니다.")
                    break

            else:
                print("홀수 입니다.")

                sel_menu_se()
                cursor = int(input())

                if cursor == 1:
                    print("계속하기")
                    continue
                elif cursor == 2:
                    print("홀짝 판별기를 종료합니다.")
                    break
                else:
                    print("잘못된 입력입니다. 종료합니다.")
                    break

        except ValueError:
            print("숫자만 입력해주세요.")
            continue


# 2. 구구단 출력기
# 원하는 단을 입력하면 그 단의 구구단을 출력하기 + 전체 보여주기

# 구구단 출력(가로)
# for x in range(2, 10):
#     str1 = str(x) + "단"
#     print(f"{str1.center(8)}", end="     ")


# for x in range(2, 10):
#     print()

#     for y in range(2, 10):
#         mul_table = str(y) + " x " + str(x) + " = " + str(x * y)
#         print(f"{mul_table.center(10)}", end="    ")

# 구구단 리스트에 담아서 (가로)
# gugudan_list = [[f"{dan} x {num} = {dan*num}" for dan in range(2, 10)] for num in range(2, 10)]
# # (가로 출력)
# for dan in range(2, 10):
#     print(f"{str(dan) + '단':^8}", end="     ")
# print()

# for row in gugudan_list:
#     for item in row:
#         print(f"{item:^10}", end="    ")
#     print()


def sel_menu_mt():
    print("=" * 20)
    print(
        """1. 전체보기
2. 선택보기
3. 종료"""
    )
    print("=" * 20)
    print("메뉴 번호를 입력해주세요. ", end="")


def multi_table():
    while True:
        print("구구단")

        try:
            sel_menu_mt()
            cursor = int(input())

            gugudan_list = [
                [f"{dan} x {num} = {dan*num}" for dan in range(2, 10)]
                for num in range(1, 10)
            ]

            # 전체보기(2-9단까지)
            if cursor == 1:

                # n단 출력
                for dan in range(2, 10):
                    print(f"{str(dan) + '단':^8}", end="     ")
                print()

                # 구구단(2-9) 가로 출력
                for row in gugudan_list:
                    for gugudan in row:
                        print(f"{gugudan:^10}", end="    ")
                    print()

                continue

            # 선택 구구단 보기
            elif cursor == 2:
                while True:
                    try:
                        dan = int(input("보고싶은 단 : "))

                    except ValueError:
                        print("잘 못 입력했습니다. 숫자를 입력해주세요.")
                        continue

                    break
                # 선택 단 출력
                print(f"{str(dan) + "단":^8}")
                # 선택 구구단 출력
                for num in range(1, 10):
                    print(f"{dan} x {num} = {dan*num}")

            elif cursor == 3:
                print("구구단을 종료합니다.")
                break

            # 메뉴 외 다른 번호 입력
            else:
                print("없는 메뉴입니다.")
                continue

        except ValueError:
            print("번호를 눌러주세요.")
            continue


# 3. 숫자 맞추기 게임
# 1-100 사이의 랜덤 숫자를 맞추는 게임 만들기


def guess_number():

    import random

    while True:
        print("숫자 맞추기")
        sel_menu_se()

        while True:
            try:
                cursor = int(input("메뉴 번호를 입력하세요. "))
            except ValueError:
                print("잘 못 입력했습니다. 숫자를 입력해주세요.")
                continue
            break

        if cursor == 1:
            answer = random.randint(1, 100)
            chance = 5

            while True:
                print(f"숫자를 맞춰보세요. 기회는 {chance} 번 입니다.")
                print(f"{"_ "*len(str(answer))}{len(str(answer))} 자리 숫자입니다.")

                # 정답보기
                print(answer)

                while True:
                    try:
                        user_guess = int(input("숫자를 입력하세요. "))
                    except ValueError:
                        print("잘 못 입력했습니다. 숫자를 입력해주세요.")
                        continue
                    break

                if answer == user_guess:
                    print(
                        f"""*정답입니다*
정답 : {answer}
추측 : {user_guess}"""
                    )
                    break

                else:
                    chance -= 1

                    if chance == 0:
                        print("기회가 모두 소진되었습니다.")
                        break
                    else:
                        print(f"틀렸습니다. 기회가 {chance} 번 남았습니다.")
                        continue

        elif cursor == 2:
            print("숫자 맞추기를 종료합니다.")
            break

        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 4. 리스트 최대/최소/합 구하기
# ex. 리스트 = [1,4,2,10,3]
# 사용자 입력 리스트로 바꾸겠음


def math_list_menu():
    print("=" * 20)
    print(
        """1. 리스트 만들기
2. 결과보기(최대값, 최소값, 합)
3. 종료"""
    )
    print("=" * 20)
    print("메뉴 번호를 입력해주세요. ", end="")


def math_list():

    num_list = []

    while True:
        print("최대값, 최소값, 합 구하기")
        math_list_menu()

        try:
            cursor = int(input())
        except ValueError:
            print("잘 못 입력했습니다. 숫자를 입력해주세요.")
            continue

        # 숫자 리스트 만들기
        if cursor == 1:
            for i in range(5):
                try:
                    user_int = int(input("넣고 싶은 숫자를 입력해주세요."))
                    num_list.append(user_int)
                except ValueError:
                    print("잘 못 입력했습니다. 숫자를 입력해주세요.")
                    continue

            print(f"생성된 숫자 리스트 : {num_list}")
            continue

        # 최대값, 최소값, 합 보기
        elif cursor == 2:
            # 파이썬에서는 리스트에 empty()가 없음 대신 not 으로 있는지 없는지 확인 가능
            if not num_list:
                print("숫자 리스트가 없습니다. 만든 후 이용해 주세요.")
                continue
            else:
                num_list.sort()
                min = num_list[0]
                max = num_list[-1]
                sum = 0
                for num in num_list:
                    sum += num

                print(
                    f"""숫자 리스트 {num_list}의 
최대값 = {max}
최소값 = {min}
숫자들의 합 = {sum} 입니다."""
                )
                continue

        # 종료
        elif cursor == 3:
            print("최대값, 최소값, 합 구하기를 종료합니다.")
            break

        # 그 외 메뉴 선택 시
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 5. 문자열 뒤집기
# 입력 : "hello"
# 출력 : "olleh"

# def string_reverse_menu():


def string_reverse():
    print("문자열 뒤집기")

    while True:
        while True:
            # 위에 만든 계속 종료 메뉴
            sel_menu_se()
            try:
                cursor = int(input())
            except ValueError:
                print("잘 못 입력했습니다. 숫자를 입력해주세요.")
                continue
            break

        if cursor == 1:
            user_str = str(
                input(
                    """뒤집고 싶은 문자열을 입력해주세요.
숫자도 가능합니다. """
                )
            )
            reverse_str = user_str[::-1]
            print(f"뒤집은 문자열 : {reverse_str}")
            continue

        elif cursor == 2:
            print("문자열 뒤집기를 종료합니다.")
            break

        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


#  6. 약분
#  분자와 분모를 입력받고 약분해서 분수 형태로 보여주기


def abbreviation():
    while True:
        print("숫자 약분하기")

        while True:
            sel_menu_se()
            try:
                cursor = int(input())
            except ValueError:
                print("잘 못 입력했습니다. 숫자를 입력해주세요.")
                continue
            break

        if cursor == 1:
            while True:
                try:
                    # 분자
                    numerator = int(input("분자를 입력해주세요. "))
                    # 분모
                    denominator = int(input("분모를 입력해주세요. "))
                except ValueError:
                    print("숫자만 입력해주세요.")
                    continue
                break

            # 약분 시작
            # 분자와 분모의 약수를 담을 리스트
            nume_list = []
            denom_list = []
            # 공통 약수를 담을 리스트
            divisor_list = []
            # 분자 약수
            for n in range(1, numerator + 1):
                if numerator % n == 0:
                    nume_list.append(n)
            # 분모 약수
            for n in range(1, denominator + 1):
                if denominator % n == 0:
                    denom_list.append(n)

            # 공통 약수 구하기
            divisor_list = list(set(nume_list) & set(denom_list))
            divisor_list.sort()

            div_nume = numerator / divisor_list[-1]
            div_denom = denominator / divisor_list[-1]

            print(
                f"""약분
{int(div_nume)}/{int(div_denom)}"""
            )

        elif cursor == 2:
            print("숫자 약분하기를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


#
#
# 메서드로 만들었으니까 통합실행 기능 추가하기


#
#
# gpt 평가
# ✅ 1. 홀짝 판별기
# ✔️ 기능 정상 작동

# ✔️ 예외 처리 (ValueError) 잘함

# ⚠️ 메뉴 선택 중복 코드 있음 → 리팩터링 가능

# ⚠️ 중복된 코드 줄이려면 메뉴 선택 함수가 반환값을 주게 만들어도 좋음

# 점수: 9/10

# ✅ 2. 구구단 출력기
# ✔️ 전체, 선택 보기 둘 다 잘 작동

# ✔️ 가로 정렬도 좋음

# ⚠️ 선택한 단 출력 시 1~9로 출력해야 하지만 1~10까지 출력되지 않아서 범위 확인 필요

# ⚠️ print(answer)로 정답을 바로 보여주는 부분은 디버깅용이라면 주석 처리 필요

# 점수: 9/10

# ✅ 3. 숫자 맞추기 게임
# ✔️ 기능 완벽 작동

# ⚠️ 정답을 바로 보여주는 print(answer) → 디버깅용 주석 필요

# ⚠️ 기회 줄어들 때 0 아래로 안 내려가는 안전장치 추가 가능

# 점수: 8.5/10

# ✅ 4. 리스트 최대/최소/합 구하기
# ✔️ 리스트 입력 잘 받아서 처리

# ✔️ 리스트 없을 때 예외 처리도 있음

# ⚠️ min, max, sum은 내장 함수 이름이기 때문에 변수 이름으로 사용하지 않는 게 좋음 (min_, sum_ 등으로)

# 점수: 8.5/10

# ✅ 5. 문자열 뒤집기
# ✔️ 역순 슬라이싱으로 잘 구현

# ✔️ 숫자도 문자열로 처리 가능

# ⚠️ 입력 안내 메시지 약간 길지만 친절해서 OK

# 점수: 10/10

# ✅ 6. 약분
# ✔️ 공약수 리스트로 구해서 최대공약수로 나누는 방식 좋음

# ⚠️ math.gcd() 활용하면 훨씬 간단해짐 (리팩터링 포인트)

# ⚠️ 나눗셈 / → 정수 결과를 원한다면 // 사용 권장

# 점수: 8/10

# ✅ 전체 구조/통합
# ✔️ 각각의 기능이 함수로 잘 나눠져 있고, 일관된 메뉴 처리 방식 사용

# ⚠️ 통합 메뉴 및 선택 실행 기능이 아직 없음 (언급만 되어 있음)

# ⚠️ 코드가 전체적으로 중복되는 부분이 있으므로 리팩터링 여지가 많음

# 💯 총평
# 총점: 53/60
# 등급: A (초급 기준 우수!)

# 구현력도 좋고, 사용자 입력이나 예외 처리도 충분히 고려했어. 지금 수준에서 더 발전하려면:

# 중복 제거 (리팩터링)

# 내장 함수 활용 (예: max, min, sum, math.gcd)

# 함수 분리 및 반환형으로 구조 더 깔끔하게 만들기
