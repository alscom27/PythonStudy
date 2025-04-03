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


# 반환값을 주려다가 밑에서 방법을 알고 다시 수정
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


def fibonacci_sequence():
    while True:
        print("피보나치 수열")

        cursor = cursor_func(menu_se)

        if cursor == 1:
            while True:
                try:
                    user_num = int(input("몇 번째까지의 피보나치 수열을 구할까요? "))
                except ValueError:
                    print("잘 못 입력했습니다. 숫자만 입력해주세요.")
                    continue
                break

            # 피보나치 수열 구하기
            fibo_list = [0, 1]
            x = 0
            y = 1
            while True:
                if user_num == 0:
                    fibo_list.pop()
                    break

                elif fibo_list[x] + fibo_list[y] <= user_num:
                    fibo_list.append(fibo_list[x] + fibo_list[y])
                    x += 1
                    y += 1
                    continue
                else:
                    break

            print(
                f"""{user_num}까지의 피보나치 수열 :
{fibo_list}"""
            )
            continue

        elif cursor == 2:
            print("피보나치 수열을 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 3. 계산기 만들기
# 두 수와 연산자(+, -, *, /)를 입력받아 계산 결과 출력
# 추가:  ^n 하면 거듭제곱 o, ! = 팩토리얼도 되게 해보자
# 등등 기능 더 추가 ex.log(n) ...까지만 추가하자

# re 모듈
# regex는 정규 표현식으로 흔히 알려져 있습니다. 파이썬에서 정규 표현식을 사용할 때, 내장 모듈인 re를 사용하고 있습니다.
# import re

# 수식을 숫자와 기호로 쪼개서 리스트로
# formula1 = "(1+4)+4*5+2(6+3)"
# formula1 = re.split("([^0-9])", formula1)
# print(formula1)
# formula1 = " ".join(formula1).split()
# print(formula1)

# SymPy는 부호(Symbol) 수학을 위한 수학 library입니다.
# import sympy as sp

# 수식을 유니코드 로 출력
# 일반 콘솔/터미널에서는 이쁘게 출력할 수 없음
# jupyter 노트북에서 display()와 사용하면 이쁘게 출력이 됨.
# sp.init_printing(use_unicode=True)

# 아래 처럼 임포트 했더니 sympy 안에 re 와 함수가 충돌해서 에러발생
# from sympy import *
# init_printing()

# from sympy import simplify, sp
# type = list , sp = import한 sympy의 alias
# dir() 안에 포함된 모든 속성, 함수, 클래스, 상수 이름 목록
# help() 터미널에서 함수나 클래스에 대해 문서화된 설명 보기 가능
# _doc_ 한줄 설명만 빠르게
# print(dir(sp))

# inspect 모듈 : 모듈/클래스 내부 구성요소를 전부 탐색하거나 필터링 탐색 가능.
# import inspect


def menu_calc():
    print("=" * 20)
    print(
        """1. 일반 계산기
2. 공학용 계산기
3. 종료"""
    )
    print("=" * 20)


# 수식을 컴퓨터가 알아들을 수 있게 수정 기능(ex. 2(4+3) -> 2*4+2*3)
def fix_formula(formula):
    import re

    # r'' = raw문자열 (있는그대로 문자 ex. hello\nworld) 정규표현식 사용을 위해 사용
    # %를 퍼센트로 인식하게 변환
    formula = re.sub(r"(\d+(?:\.\d+)?)%", r"(\1/100)", formula)

    formula = re.sub(
        r"(\d)(\()", r"\1*\2", formula
    )  # 앞에 숫자가 있고 바로 뒤에 '(' 여는 괄호가 있으면 1번그룹과 2번 그룹 사이에 * 추가
    formula = re.sub(
        r"(\))(\d)", r"\1*\2", formula
    )  # ')'닫는 괄호 뒤에 바로 숫자가 있다면 1그룹 2그룹 사이에 *추가
    formula = re.sub(
        r"(\))(\()", r"\1*\2", formula
    )  # ')'닫는 괄호 뒤에 '('여는 괄호가 있다면 사이에 * 추가

    return formula


# 위에 기능을 공학용 계산기로도 사용할 수 있게
def fix_sci_formula(formula):

    import re

    formula = re.sub(r"(\d+(?:\.\d+)?)%", r"(\1/100)", formula)

    formula = re.sub(
        r"(\d)(\()", r"\1*\2", formula
    )  # 앞에 숫자가 있고 바로 뒤에 '(' 여는 괄호가 있으면 1번그룹과 2번 그룹 사이에 * 추가
    formula = re.sub(
        r"(\))(\d)", r"\1*\2", formula
    )  # ')'닫는 괄호 뒤에 바로 숫자가 있다면 1그룹 2그룹 사이에 *추가
    formula = re.sub(
        r"(\))(\()", r"\1*\2", formula
    )  # ')'닫는 괄호 뒤에 '('여는 괄호가 있다면 사이에 * 추가

    # 여기까진 위에 기본기능으로 만들어 놓은 기능
    # 공학용 추가

    # 제곱근(root)
    # 정수√정수 일 때 , 제곱근의 파라미터가 2개일 때, n제곱근
    formula = re.sub(r"(\d+)√(\d+|\([^\(\)]+\))", r"root(\2, \1)", formula)

    # 단순히 루트 기호만 있을 경우
    # 제곱근의 파라미터가 1개 , 제곱근 전용
    formula = formula.replace("√", "sqrt(")
    formula = re.sub(r"sqrt\(([^()]+)\)", r"sqrt(\1)", formula)

    # factorial (!)
    # 숫자 또는 괄호 뒤에 !가있으면 ! 앞의 그룹(1)을 factorial(1번 그룹) 으로 치환
    formula = re.sub(r"(\d+|\([^\(\)]+\))!", r"factorial(\1)", formula)

    # log 함수 변환
    formula = formula.replace("log10", "log")  # sympy의 log는 log10
    formula = re.sub(r"log2\(([^)]+)\)", r"log(\1, 2)", formula)  # log2(x) → log(x, 2)
    formula = formula.replace("ln", "log")  # ln(x) → log(x)

    # π, e 상수
    formula = formula.replace("π", "pi")
    formula = formula.replace("Π", "pi")  # 대문자도 대응
    formula = formula.replace("e", "E")  # sympy의 자연상수는 E

    return formula


def calculating_machine():

    import sympy as sp

    while True:
        print("계산기")

        cursor = cursor_func(menu_calc)

        # 일반 계산기
        if cursor == 1:
            while True:
                print("일반 계산기")
                # 사용자 수식ㅇ입력
                user_formula = input("수식을 입력해 주세요. ")

                # 입력받은 수식을 계산

                # 사칙연산
                fixed_formula = fix_formula(user_formula)
                try:
                    answer = eval(fixed_formula)
                except NameError:
                    print("다시 입력해주세요.")
                    continue
                break

            print(
                f"""요청 수식 : {user_formula}
답 = {answer}"""
            )

            continue

        # 공학용 계산기
        elif cursor == 2:
            print("공학용 계산기")
            # 사용자 수식ㅇ입력
            user_formula = input("수식을 입력해 주세요. ")

            # 입력받은 수식을 계산

            # 수식 치환
            fixed_sci_formula = fix_sci_formula(user_formula)

            # 문자열을 sympy 수식으로 변환
            # sympify는 sympy의 수식 객체를 반환
            sy_formula = sp.sympify(fixed_sci_formula)

            # 계산
            # 흰색으로 표시되는 이유는 클래스의 메서드이기 때문에
            answer = sy_formula.evalf()

            # 몇 몇 안되는 수식들이 있음...

            print(
                f"""요청 수식 : {user_formula}
답 = {answer}"""
            )

            continue

        elif cursor == 3:
            print("계산기를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 4. 숫자 야구 게임
# 3자리 숫자를 랜덤으로 만들고 ,사용자가 맞히는 게임
# 예: 123 vs 132 -> 1S 2B
# 이건 뭔 게임인지 몰라 찾아보자. (물어봄)
#  기본 규칙
# 숫자 구성
# 상대방(또는 컴퓨터)은 서로 다른 숫자로 이루어진 3자리 숫자를 몰래 정해.
# 예: 427 (숫자 중복 없음)
# 플레이어가 추측
# 플레이어는 그 숫자가 뭔지 추측해서 입력해.
# 예: 내가 123이라고 입력했다고 해보자.
# 판정 결과: 스트라이크(Strike)와 볼(Ball)
# Strike (S): 숫자와 위치가 모두 맞음
# Ball (B): 숫자는 맞지만, 위치가 틀림
# 예를 들어, 정답이 427이고 내가 123을 입력했다면:
# 2는 정답에도 있고 위치도 맞음 → 1S
# 1, 3은 정답에 없음 → 0B
# 결과: 1 Strike, 0 Ball (1S 0B)


def number_baseball():

    import random

    while True:
        print("숫자 야구 게임")

        cursor = cursor_func(menu_se)

        # 숫자 야구 게임 시작
        if cursor == 1:

            # 맞춰야 할 숫자 생성 근데 숫자 중복 없이
            rand_num_list = []
            while True:
                rand_num = random.randint(0, 9)
                rand_num_list.append(rand_num)
                remove_distinc = set(rand_num_list)

                if len(remove_distinc) == 3:
                    rand_num_list = list(remove_distinc)
                    if rand_num_list[0] != 0:
                        break

            # 콘솔에 보여지는 맞춰야 할 숫자
            view_num = []
            # 3은 나중에 난이도로도 바꿀 수 있음.
            for n in range(3):
                view_num.append("_")

            print(f"맞춰야 할 숫자 : {view_num}")

            while True:
                user_input_idx = input("몇 번째 자리를 추측하시겠습니까? ").strip()
                user_input_guess = input("추측할 숫자 입력 (0~9) : ").strip()

                if user_input_idx.isdigit() & len(user_input_idx) == 1:
                    user_idx = int(user_input_idx)
                    if user_input_guess.isdigit() & len(user_input_guess) == 1:
                        user_guess = int(user_input_guess)
                        break

                    else:
                        print("한 자리 숫자만 입력해주세요.")
                        continue
                else:
                    print("한 자리 숫자만 입력해주세요.")
                    continue

            # score 기록
            score = {"S": 0, "B": 0}
            strike_count = 0
            ball_count = 0
            if user_guess in rand_num_list:
                for i in range(len(rand_num_list) + 1):
                    # 숫자와 위치가 맞은 경우
                    if rand_num_list[i] == user_guess & i == user_idx:
                        print("Strike!")
                        strike_count += 1
                        score.update({"S": strike_count, "B": ball_count})
                        view_num[i] = user_guess

        elif cursor == 2:
            print("숫자 야구 게임을 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 5. 학생 성적 관리 프로그램
# 여러 명의 이름과 점수를 입력받고, 평균/최고점/정렬 등을 출력


number_baseball()
