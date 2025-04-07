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

# eval() 함수는 입력받은 데이터를 바로 파이썬 코드로 변환하기 때문에 command injection 방법으로 해킹 위험 있음.


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

                    else:
                        rand_num_list = []
                        continue

            # 콘솔에 보여지는 맞춰야 할 숫자
            view_num = []
            # 3은 나중에 난이도로도 바꿀 수 있음.
            for n in range(3):
                view_num.append("_")

            # 시도 횟수 카운트
            chance = 0
            # score 기록
            score = {"S": 0, "B": 0}
            strike_count = 0
            ball_count = 0

            while True:
                print(f"맞춰야 할 숫자 : {view_num}")
                user_input_idx = input(
                    "몇 번째 자리를 추측하시겠습니까? (1~3) "
                ).strip()
                user_input_guess = input("추측할 숫자 입력 (0~9) : ").strip()

                #  | 는 비트 or 논리적 판단에는 맞지 않음. or 사용
                if (
                    not user_input_idx.isdigit()
                    or len(user_input_idx) != 1
                    and user_idx > 0 & user_idx <= 3
                ):
                    print("한 자리 숫자만 입력해주세요.")
                    continue

                # continue 뒤에 조건문이 들여쓰기 되어있다면 절대 실행되지 않음.
                if (
                    not user_input_guess.isdigit()
                    or len(user_input_guess) != 1
                    and user_guess >= 0 & user_guess <= 9
                ):
                    print("한 자리 숫자만 입력해주세요.")
                    continue

                user_idx = int(user_input_idx) - 1
                user_guess = int(user_input_guess)
                chance += 1

                # 문제에 추측 번호가 있으면
                if user_guess in rand_num_list:
                    for i in range(0, len(rand_num_list)):

                        # 숫자와 위치가 맞은 경우
                        # if rand_num_list[i] == (user_guess & i == user_idx) : &가 파이썬에서 비트연산자라 이렇게 표현이 됨.
                        if rand_num_list[i] == user_guess and i == user_idx:
                            # 이미 맞춘게 아니라면
                            if view_num[i] == "_":
                                print("Strike!")
                                strike_count += 1
                                score.update({"S": strike_count, "B": ball_count})
                                view_num[i] = user_guess

                                print(
                                    f"""현재 스코어 : {score}
시도 횟수 : {chance}"""
                                )

                        # 숫자가 있긴한데 위치가 틀린 겨우
                        # 이미 맞춘 번호에 대해서 계속해서 볼카운트 추가되는 현상 고치기
                        else:
                            # 이미 오픈되어 있는 숫자가 아닌 경우
                            if not user_guess in view_num:
                                print("Ball")
                                ball_count += 1
                                score.update({"S": strike_count, "B": ball_count})
                                print(
                                    f"""현재 스코어 : {score}
시도 횟수 : {chance}"""
                                )
                            continue

                # 아예 틀린 경우
                else:
                    print("틀렸습니다.")
                    print(
                        f"""현재 스코어 : {score}
시도 횟수 : {chance}"""
                    )
                    continue

                # 이겻을 때
                if strike_count == 3:
                    print(
                        f"""현재 스코어 : {score}
시도 횟수 : {chance}
승리!"""
                    )
                    break

        elif cursor == 2:
            print("숫자 야구 게임을 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 5. 학생 성적 관리 프로그램
# 여러 명의 이름과 점수를 입력받고, 평균/최고점/정렬 등을 출력


# 학생 성적 관리_메뉴
import re


def menu_grade_mange():
    print("=" * 20)
    print(
        """1. 학생 성적 등록하기
2. 그만 등록하기/종료
3. 성적 조회하기"""
    )
    print("=" * 20)


def menu_grade_sel():
    print("=" * 20)
    print(
        """1. 학생 성적 검색하기
2. 성적 조회 종료하기"""
    )
    print("=" * 20)


def grade_management():
    while True:
        print("학생 성적 관리")

        cursor = cursor_func(menu_se)

        if cursor == 1:
            # 학생(key) 과목(value) 별로 담은 dict
            stu_class_dict = dict()
            # 과목(key) 점수(value) 별로 담은 dict
            class_score_dict = dict()
            # 과목 등록
            class_name_input = input(
                "등록할 과목을 입력해주세요.(띄어쓰기와 ','로 구분됩니다.) "
            )
            while True:

                cursor = cursor_func(menu_grade_mange)
                # 하나씩 등록
                if cursor == 1:
                    print("※ 한 명씩 등록해주세요.")

                    # 반복
                    while True:

                        stu_name_input = input("학생 이름을 입력해주세요. ")

                        # class_name_list = class_name_input.split(",")
                        class_name_list = [
                            class_name
                            for class_name in re.split(
                                r"[,\s]+",
                                class_name_input.strip(),
                                # 생명 과학 같이 띄어쓰기 필요할 것 같아서 , 로만 나누다가 공백포함해서 값이 들어가서 공백으로도 구분되게 바꿈
                                # r"[,]+",class_name_input.strip(),
                            )
                            if class_name
                        ]
                        for class_name in class_name_list:
                            class_score_dict[class_name] = 0

                        for class_name in class_score_dict.keys():
                            while True:
                                try:
                                    score_input = int(
                                        input(
                                            f"{stu_name_input}의 {class_name} 점수를 입력해주세요. "
                                        )
                                    )
                                    class_score_dict[class_name] = score_input
                                    break

                                except ValueError:
                                    print("점수는 숫자만 입력해주세요.")
                                    continue

                        stu_class_dict[stu_name_input] = class_score_dict
                        break

                elif cursor == 2:
                    # 자바에는 isEmpty()가 있지만 파이썬은 없고 비어있으면 false를 반환
                    if bool(stu_class_dict) == False:
                        print("등록된 학생이 없습니다. 이전 메뉴로 돌아갑니다.")
                        break
                    else:
                        print("등록하기를 멈춥니다.")
                        break

                # 성적 조회
                elif cursor == 3:

                    # 조회할 학생이 있으면
                    if bool(stu_class_dict) == True:

                        # 학생들의 과목별 평균, 최고점

                        # 과목별 평균 dict
                        class_avg_dict = dict()
                        # 과목별 최고점 dict
                        class_max_dict = dict()
                        for class_name in class_score_dict.keys():
                            sum_score = 0
                            avg_score = 0
                            max_score = 0
                            for student_name in stu_class_dict.keys():
                                # 한 학생에 대한 과목별 점수 dict
                                stu_class_score_dict = stu_class_dict[student_name]
                                score = stu_class_score_dict[class_name]
                                # 평균
                                sum_score = score
                                avg_score = sum_score / len(list(stu_class_dict.keys()))
                                class_avg_dict[class_name] = avg_score
                                # 최고점
                                if max_score < score:
                                    max_score = score
                                    class_max_dict[class_name] = max_score
                        # 결과 출력
                        # 보고싶은 학생을 검색할 수 있게

                        while True:

                            cursor = cursor_func(menu_grade_sel)

                            # 조회하기
                            if cursor == 1:

                                search_stu = input("검색할 학생명을 입력해주세요. ")
                                if search_stu in stu_class_dict.keys():
                                    print("=" * 20)
                                    print(f"{search_stu}학생 성적")
                                    print(
                                        f"{'과목':<10} | {'점수':<9} | {'과목별 평균':<6} | {'과목별 최고점':<10}"
                                    )
                                    for class_name in class_score_dict.keys():
                                        print(
                                            f"{class_name:<10} | 점수 : {class_score_dict[class_name]:<4} | 평균 : {class_avg_dict[class_name]:<4.2f} | 최고점 : {class_max_dict[class_name]:<3}"
                                        )
                                    #     print(
                                    #         f"{class_score_dict[class_name]}/{class_avg_dict[class_name]}/{class_max_dict[class_name]}",
                                    #         end=" ",
                                    #     )
                                    # print()
                                    print("=" * 20)

                                else:
                                    print("명단에 없는 학생입니다. 다시 입력해주세요.")
                                    continue

                            elif cursor == 2:
                                print("학생 성적 조회를 종료합니다.")
                                break
                            else:
                                print("없는 메뉴입니다. 다시 선택해주세요.")
                                continue

                    # 조회를 할 때 입력받은 학생들이 없으면
                    else:
                        print("조회할 성적이 없습니다.")
                        continue

        elif cursor == 2:
            print("학생 성적 관리를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


######################################
# gpt 평가
# ✅ 1. 소수 판별기
# ✔️ 1과 자기 자신만 나눠지는 수 정의에 맞게 구현

# ✔️ 예외 처리, 메뉴 선택 구조 완성도 높음

# ⚠️ 리스트에 모든 약수를 다 담기보다, 2부터 √n 까지만 나눠봐도 충분함 (성능 개선 포인트)

# 점수: 9/10

# ✅ 2. 피보나치 수열 출력
# ✔️ 수열 출력 구조 잘 되어 있음

# ⚠️ 현재 로직은 n번째 피보나치 수가 아니라 n 이하까지의 피보나치 수열 출력으로 보임 → 문제 정의와 다름

# ⚠️ 0 입력 시 처리도 있어서 안정성 OK

# 점수: 8.5/10

# ✅ 3. 계산기 (일반/공학용)
# ✔️ 일반 계산기: 괄호/연산자 입력 및 수식 처리 깔끔함

# ✔️ 공학용 계산기: √, %, !, log, π, e 등 정규표현식 기반 치환 너무 잘 구현됨

# ✔️ sympy 사용도 잘 활용

# ⚠️ eval() 사용은 제한된 환경에선 위험할 수 있으니 ast.literal_eval() 또는 math 기반 eval 사용 고려

# ⚠️ UI적으론 좀 길지만 중급 수준에서는 매우 훌륭함

# 점수: 9.5/10

# ✅ 4. 숫자 야구 게임
# ✔️ 숫자 랜덤 생성 + 중복 방지, Strike/Ball 판정 정확

# ✔️ 추측 위치별 처리도 잘 되어 있음

# ⚠️ user_idx > 0 & user_idx <= 3 → 이건 &가 아니라 and / 괄호로 묶지 않아서 버그 발생 가능성 있음

# ⚠️ 중복된 숫자 추측에 대한 처리(볼 카운트 중복 방지)는 잘 고려됨

# ⚠️ 변수 위치가 중간에 초기화되는 부분이 혼동 줄 수 있음

# 점수: 8.5/10

# ✅ 5. 학생 성적 관리 프로그램
# ✔️ 구조가 복잡하지만 잘 나눠져 있음 (메뉴 → 등록/조회 → 검색)

# ✔️ 과목 여러 개 입력, 평균/최고점 처리 잘 구현됨

# ✔️ re.split()로 공백과 쉼표 동시에 처리한 것도 좋음

# ⚠️ 딕셔너리 복사 문제 발생 가능: class_score_dict를 모든 학생에게 동일한 객체로 넣고 있어서 모든 학생 점수가 덮어쓰여짐 → copy() 또는 새로 선언 필요

# ⚠️ sum_score = score 로 누적되지 않고 마지막 점수로 덮어써짐 → 누적하려면 sum_score += score 사용해야 함

# python
# 복사
# 편집
# # 이 부분은 반드시 수정 필요!
# class_score_dict[class_name] = 0
# ...
# stu_class_dict[stu_name_input] = class_score_dict  # 이건 모든 학생이 같은 dict를 공유함
# 점수: 7.5/10

# 💯 총평
# 문제	점수
# 1. 소수 판별기	9.0
# 2. 피보나치 수열	8.5
# 3. 계산기	9.5
# 4. 숫자 야구 게임	8.5
# 5. 학생 성적 관리	7.5
# 총점	43 / 50
# 등급: A- ~ B+ (중급 기준 상위권, 다만 일부 중요한 구조적 실수 존재)

# ✅ 개선 방향 제안
# 딕셔너리 복사 이슈 (성적 관리) → 꼭 dict.copy() 또는 deepcopy() 고려

# 수식 계산기 리팩터링 → 정규표현식 치환 부분만 함수로 따로 뽑으면 유지보수 쉬움

# eval() 사용 시 보안 주의

# 사용자 입력 숫자 검사에 and, 괄호 누락 등 조심
