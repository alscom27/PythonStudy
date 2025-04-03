# id() : 값이 메모리에 할당된 주소를 알려줌

a = [1, 2, 3]
print(id(a))
b = a
print(id(a))
print(id(b))

print(a is b)

# 리스트에서 값을 바꿀때 다른 변수에 담았더라도 같이 바뀜
# 일반적으로는 다르게 동작
a[0] = 4
print(a)
print(id(a))
print(b)
print(id(b))


a = [1, 2, 3]
b = a[:]  # 이렇게하면 값은 같이 바뀜 할당된 주소가 다름
print(id(a))
print(a)
print(id(b))
print(b)

# copy 임포트
from copy import copy

aa = [1, 2, 3]
print(id(aa))
bb = copy(aa)
print(id(bb))
# copy는 아예 독립되게 만듬 주소도 값도 다르게 할 수있음
print(a is b)
print(id(aa))
print(id(bb))

aa[0] = 4
print(aa)
print(bb)

# 원본에 영향을 미치지 않아야 하는경우에는 deepcopy 사용


a = [1, 2, 3]
a = a + [4, 5]
# 주소가 달라짐
# 위와 아래 값은 같지만 할당되는 주소가 다름
# 주소가 같음
a = [1, 2, 3]
a.extend([4, 5])


# condition
age = 19

if age < 20:
    print("청소년 할인")


work_count = 2000
if work_count >= 1000:
    print("목표 달성")


game_score = 800
if game_score >= 1000:
    print("당신은 고수입니다.")
else:
    print("당신은 하수입니다.")


num_a = 100
num_b = 200
if num_a == num_b:
    print("두 값이 일치합니다.")
else:
    print("두 값이 일치하지 않습니다.")

# score = int(input("당신의 점수는 얼마입니까?"))

# match-case 문에서 case에 >, < 등 비교연산은 사용불가 굳이 하고싶다면 case 문에 if를 사용해야함


lucky_list = [1, 9, 23, 46]

no = 23
print("야호" if no in lucky_list else "꽝")

age = 30
height = 180
print("Yes" if age < 30 & height >= 170 else "No")

i = 0
while i < 5:
    print("Welcom")
    i += 1


st = "Programming"

for ch in st:
    if ch in ["a", "e", "i", "o", "u"]:
        break
    print(ch)

tree_hit = 0
while tree_hit < 10:
    tree_hit += 1
    print(f"나무를 {tree_hit}번 찍었습니다.")

    if tree_hit == 10:
        print("나무 넘어갑니다.")

#
num_list = [1, 2, 6, 3, 4, 5]
num_list.sort()


# 입력 필요해서 주석
# prompt = """1. Add
# 2. Delete
# 3. List
# 4. Quit
# Enter number : """
# number = 0
# while number != 4:
#     print(prompt)
#     try:
#         number = int(input("숫자 입력 : "))
#     except ValueError:
#         print("숫자만 입력!")
#         continue


# # 커피 자판기
# import random

# while True:
#     coffee = random.randint(1, 10)

#     money = int(input("돈을 넣어주세요 : "))

#     if money == 300:
#         print("커피를 줍니다.")
#         coffee -= 1
#     elif money > 300:
#         print(f"거스름돈 {money-300}원을 주고 커피를 줍니다.")
#         coffee -= 1
#     else:
#         print(
#             f"""돈을 다시 돌려주고 커피를 주지 않습니다.
# 남은 커피의 양은 {coffee}개 입니다."""
#         )


# 1부터 100 까지의 자연수 모두 더하고 그 결과
sum = 0
for n in range(1, 101):
    sum += n

print(sum)

# 1부터 100 까지 자연수 중 3의 배수의 합은
sum = 0
# for n in range(1, 101):
#     if n % 3 == 0:
#         sum += n
# print(sum)

for n in range(3, 101, 3):
    sum += n
print(sum)


# 리스트에서 50점 이상의 점수들의 총합을 구하시오.
a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for score in a:
    if score >= 50:
        sum += score
print(sum)

n = 0
while n < 4:
    n += 1
    print("*" * n)


numbers = [11, 22, 33, 44, 55, 66]
for n in numbers:
    print(n, end=" ")

summer_fruits = ["수박", "참외", "체리", "포도"]

print()
for fruit in summer_fruits:
    print(fruit, end=" ")

print()

# 구구단
gugudan_list = [
    [f"{dan} x {num} = {dan*num}" for dan in range(2, 10)] for num in range(1, 10)
]

# 단출력
for dan in range(2, 10):
    print(f"{str(dan) + "단":^8}", end="     ")
print()
# 구구단 가로 출력
for row in gugudan_list:
    for gugudan in row:
        print(f"{gugudan:^10}", end="    ")
    print()


e = list(range(0, -10, -1))
print(e)

num = 10
for n in range(num):
    print(n)
