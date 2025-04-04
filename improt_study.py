import numpy as np

# 파이썬으로 수치해석, 통계 관련 기능을 구현한다고 할 때 NumPy는 가장 기본이 되는 모듈이다.


print(type(np.arange(0, 10, 0.5)))  # type = numpy.ndarray


print(np.arange(10, 0, -0.7))

print(list(range(0, 10, 2)))
print(list(range(1, 10, 2)))
print(list(range(-2, -10, -2)))

test_list = ["one", "two", "three"]
for i in test_list:
    print(i)

# 리스트안에 튜플 for문 돌리기
a = [(1, 2), (3, 4), (5, 6)]
for first, last in a:
    print(first, end=" ")
    # print(last, end=" ")
    # print(f"{first} , {last}", end="  ")
print()

for t in a:
    print(t[0] + t[1])


list1 = list()
for i in range(3, 10, 3):
    list1.append(i)

print(list1)


result = [num * 3 for num in range(1, 5)]
print(result)


result = tuple([({x}, {y}) for x in range(2, 10) for y in range(1, 10)])
print(type(result))


# 근의 공식
def get_root(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2


result1, result2 = get_root(1, 2, -8)
print(f"해는 {result1} 또는 {result2}")


import math
import random
import datetime

print(math.pi)
print(math.sin(3.14))
print(random.random())
# 주사위
print(int(random.random() * 6 + 1))
print(random.randint(1, 6))

print(datetime.datetime.now())
