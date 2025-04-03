# ############## library ################

# re 모듈
# regex는 정규 표현식으로 흔히 알려져 있습니다. 파이썬에서 정규 표현식을 사용할 때, 내장 모듈인 re를 사용하고 있습니다.
import re

# 수식을 숫자와 기호로 쪼개서 리스트로
# formula1 = "(1+4)+4*5+2(6+3)"
# formula1 = re.split("([^0-9])", formula1)
# print(formula1)
# formula1 = " ".join(formula1).split()
# print(formula1)

# SymPy는 부호(Symbol) 수학을 위한 수학 library입니다.
import sympy as sp

# 수식을 유니코드 로 출력
# 일반 콘솔/터미널에서는 이쁘게 출력할 수 없음
# jupyter 노트북에서 display()와 사용하면 이쁘게 출력이 됨.
sp.init_printing(
    use_unicode=True
)  # inspect 모듈 : 모듈/클래스 내부 구성요소를 전부 탐색하거나 필터링 탐색 가능.
import inspect

# sympy 안에 모든 함수
# sympy_builtins = [
#     name for name, obj in inspect.getmembers(sp) if inspect.isfunction(obj)
# ]
# print(sympy_builtins)

# sympy 안에 키워드로 필터링해서 뽑은 함수
# keywords = ["add", "sub", "mul", "div", "mod", "pow", "simplify", "expand"]


keywords = ["fact"]

ops = [
    name
    for name, obj in inspect.getmembers(sp)
    if inspect.isfunction(obj) and any(k in name.lower() for k in keywords)
]

print(" keyword 필터링 함수")
for name in ops:
    # discrip = name.__doc__  이건 error name은 함수이름을 담은 문자열이기 때문에
    func = getattr(sp, name)
    discrip = func.__doc__ or "No docstring"
    print(f"{name} : {discrip}")
