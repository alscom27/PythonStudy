#
#
#

# lambda

sum = lambda a, b: a + b
print(sum(3, 4))


my_list = [lambda a, b: a + b, lambda a, b: a * b]
my_list[0](3, 4)
print(my_list)
print(my_list[1](3, 4))

# print(lambda x, y: x + y)


add = lambda x, y: x + y
print(add(100, 200))
print(type(add))
print("100과 200의 합 :", (lambda x, y: x + y)(100, 200))

f = lambda *x: max(x) * 2
print(f(1, 2, 5, 7, 200))

f = [lambda x: x + 1, lambda x: x + 2, lambda x: x + 3]
print(f[0](1))
print(f[1](1))

dic1 = {"add": lambda x, y: x + y, "sub": lambda x, y: x - y, "mul": lambda x, y: x * y}
print(dic1["add"](3, 4))
print(dic1["sub"](3, 4))

#
print("200 - 100 =", (lambda x, y: x - y)(200, 100))

f = lambda x: x > 0
print(list(filter(f, range(-5, 5))))


# list(filter(함수, 범위))
list1 = [1, 2, 3, 4, 5, 6, 7]
f = lambda x: x % 2 == 0
print(list(filter(f, list1)))


def func(x):
    if x > 0:
        return x
    else:
        # filter에서 사용된건 bool반환이라 값을 변경하지않음
        # 그러므로 모든 값을 참으로 간주함...
        return x - 100


print(list(filter(func, range(-5, 5))))


ages = [34, 39, 20, 18, 13, 54]
print("성인 리스트")
for a in filter(lambda x: x >= 19, ages):
    print(a, end=" ")
print()

# 음수값을 추출하는 기능을 위한 필터 함수
# def minus_func(n):
#     if n < 0:
#         return True
#     else:
#         return False


n_list = [-30, 45, -5, -90, 20]
# minus_list = list()
# for n in filter(minus_func, n_list):
#     minus_list.append(n)

# print("음수 리스트 :", minus_list)

# lambda로
# for n in filter(lambda n: n < 0, n_list):
#     minus_list.append(n)

# print("음수 리스트 :", minus_list)

# 더 줄인다면
minus_list = list(filter(lambda n: n < 0, n_list))
print(minus_list)


# 문제
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda n: n % 2 == 0, n_list))
print(even_list)

odd_list = list(filter(lambda n: n % 2 != 0, n_list))
print(odd_list)


def square(x):
    return x**2


a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(square, a))
print(square_a)

# 문제
a_list = ["a", "b", "c", "d"]


def to_upper(c):
    return c.upper()


upper_a_list = list(map(to_upper, a_list))
print(upper_a_list)

# 위를 람다로
upper_a2_list = list(map(lambda c: c.upper(), a_list))
print(upper_a2_list)

twice_list = list(map(lambda x: x * 2, range(1, 10)))
print(twice_list)

# zip함수
# 패킹 언패킹
a = "YUN"
b = [1, 2, 3]
c = ["하나", "둘", "셋"]

print(list(zip(a, b, c)))
print(set(zip(a, b, c)))
# print(dict(zip(a, b, c)))s

L1 = ["a", "b", "c", "d"]
scores = [1, 2, 3]
for i, j in zip(L1, scores):
    print(i, j)

numbers = [
    [
        1,
        2,
        3,
    ],
    [4, 5, 6],
]
print(numbers)
print(*numbers)
# print(type(*numbers)) 에러
print(list(zip(*numbers)))

from functools import reduce

a = [1, 2, 4]
n = reduce(lambda x, y: x + y, a)
print(n)

sum = reduce(lambda x, y: x + y, range(1, 101))
print(sum)

facto = reduce(lambda x, y: x * y, range(1, 11))
print(facto)

# 리스트 축약표현식

a = [x**2 for x in a]
print(a)

a = ["welcom", "to", "the", "python", "world"]
first_a = [s[0] for s in a]
print(first_a)

# 반복자 iterator
import numpy as np

_str = iter("1234")
_tuple = iter((1, 2, 3, 4))
_list = iter([1, 2, 3, 4])
_dict = iter({"a": 1, "b": 2, "c": 3})
_set = iter({1, 2, 3})
_array = iter(np.array([[1, 2], [3, 4]]))
print(next(_str))
print(next(_str))
