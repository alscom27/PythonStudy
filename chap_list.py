# 리스트

fruits = ["banan", "apple", "orange", "kiwi"]
print(type(fruits))
print(fruits)

# type() ()안에 타입을 알 수 있음.
mixed_list = [100, 200, 400, "apple"]
print(type(mixed_list))
print(mixed_list)

list1 = list()
list2 = []
# 튜플을 리스트로
list3 = list((1, 2, 3))
print(list3)

# tuple(list2) 리스트를 튜플로
# dict : 딕셔너리(java의 map)

# range(1, n) 1부터 n-1까지
list4 = list(range(1, 10))
print(list4)

# 1부터 10까지 숫자중 짝수로 리스트 생성
num_list = []

for num in range(1, 11):
    if num % 2 == 0:
        num_list.append(num)

print(num_list)
# range() 함수를 이용하여 1번 문제

# 한국, 중국, 인도, 네팔의 네 원소 리스트로 만들기
# nations = ['Korea', 'China', 'India', 'Nepal']
nations = []
# match-case 자바의 switch-case 문과 같음 파이선 3.10버전 이상부터 가능
for num in range(1, 5):
    match num:
        case 1:
            nations.append("Korea")
        case 2:
            nations.append("China")
        case 3:
            nations.append("India")
        case 4:
            nations.append("Nepal")
        case _:
            nations


print(nations)

# 친구 5명 이름을 원소로 가지는 리스트
friends = ["준선", "준선이", "준선핑", "김준선", "존시나"]
print(friends)

prime_list = [2, 3, 5, 7]
print(f"prime_list의 첫 원소:{prime_list[0]}")
print("prime_list의 첫 원소: %d" % (prime_list[0]))
print("prime_list의 첫 원소: {}".format(prime_list[0]))

print("prime_list의 마지막 원소 : ", prime_list[len(prime_list) - 1])
print("prime_list의 마지막 원소 : ", prime_list[-1])

nations = ["Korea", "China", "India", "Nepal"]
print("nations의 첫 원소 : ", nations[0])

print("nations의 마지막 원소 : ", nations[-1])

print("natoins의 마지막 원소 : ", nations[len(nations) - 1])

# 리스트의 슬라이싱
a_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(a_list[1:5])
print(a_list[0:1])
print(a_list[0:2])
print(a_list[0:5])
print(a_list[1:])
print(a_list[:5])

print(a_list[-2:])
print(a_list[:-2])
print(a_list[::-1])  # 모든 항목을 가져오되 역순으로 슬라이싱
print(sorted(a_list, reverse=True))
print(a_list.sort())  # == none이 나옴 먼저 sort()해서 변수에 담고 출력은 가능
print(a_list[1::-1])  # 처음부터 2개의 항목을 가져오는데 역순으로
print(
    a_list[2:6:2]
)  # a_list[start:end:step] : start부터 end-1까지를 step만큼 건너뛰며 슬라이싱


# range(15) 함수를 사용하여 다음과 같은 리스트 생성
n_list = []

for num in range(15):
    n_list.append(num)

print(n_list)

# 문제 1번의 n_list로부터 슬라이싱을 수행 다음과 같은 리스트 생성

s_list = n_list
# s_list1 = [0,1,2,3,4]
print(s_list[:5])
# s_list2 = [5,6,7,8,9,10]
print(s_list[5:11])
# s_list3 = [11,12,13,14]
print(s_list[11:])
# s_list4 = [2,4,6,8,10]
print(s_list[2:11:2])
# s_list5 = [10,9,8,7,6]
print(s_list[10:5:-1])
# s_list6 = [10,8,6,4,2] 역순으로 2씩 건너뛰면서 슬라이싱
print(s_list[10:1:-2])

# 리스트 연산자
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a * 3)
print(str(a) + " hi")
# print(int(a)) TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# print(a * b) TypeError: can't multiply sequence by non-int of type 'list'

print(a == b)  # boolean 반환
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 == list2)
print(type(list1) == type(list2))  # 마찬가지

# 리스트 비교연산자 사용
# 문자열의 경우 사전적 순서로 비교 boolean 반환
list3 = [2, 3, 3, 4]
print(list1 > list3)

a = [1, 2, 3]
a[1] = 4
print(a)

# list가 통째로 들어감
a = [1, 2, 3]
a[1] = ["a", "b", "c"]
print(a)

# list가 풀리면서 element로 들어감
a = [1, 2, 3]
print(a[1:2])
a[1:2] = ["a", "b", "c"]
print(a)

a = [1, 2, 3]
a[1:3] = []
print(a)
# [1]

a = [1, 2, 3]
a[2] = []
print(a)
# [1, 2, []]

a = [1, 2, 3]
del a[1:3]
print(a)
# [1]

# * 인덱스로 줄 때와 범위로 줄 대가 다름 주의

n_list = [11, 22, 33, 44, 55, 66]
del n_list[3]
print(n_list)

# append와 extend 차이
# 하나만 추가 , 여러요소를(풀어서) 추가
a = [1, 2, 3]
a.append([4, 5])
print(a)

a.extend([6, 7])
print(a)

# remove와 pop 차이
# 값으로 삭제 | 리턴 x , 인덱스로 삭제 | 리턴 o
a.remove(7)
print(a)
b = a.pop(4)
print(b)  # pop()한 걸 변수에 담아야 볼 수 있음
print(a)

a.reverse()
print(a)

a = ["이순신", "강감찬", "을지문덕"]
a.sort()
print(a)

print(sorted(a, reverse=True))  # a.reverse()와 같음

list1 = [20, 10, 40, 50, 30]
list1.sort()
print(list1)

list1.sort(
    reverse=True
)  # sorted(list1, reverse=True) , list1.reverse(), list1[::-1] 과 같음 (역순)
print(list1)

a = [1, 2, 3]
print(a.index(2))
# print(a.index(4)) # ValueError: 4 is not in list

# java의 try catch문 파이썬에서는 try except문
try:
    print(a.index(4))
except ValueError:
    print("ValueError 발생")


# insert는 append(뒤에서 부터 붙이는)와 달리 위치를 지정해서 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)  # 앞에 있는 3만 지움
print(a)

a = [1, 2, 3]
a.pop()  # 뒤에서부터 빠짐
print(a)

list1 = ["a", "b", "c", "d"]
list1.remove(list1[-1])
print(list1)

# 예제
# 1.
a = [1, 2, 3]
b = [10, 20, 30]

a.append(b)
print(a)

a = [1, 2, 3]
a.extend(b)
print(a)

# 2.
nlist = []
for num in range(1, 11):
    nlist.append(num)

print(nlist)

nlist = list(range(1, 11))
print(nlist)

# 3.
nlist.insert(0, 0)
print(nlist)

# 4.
nlist.reverse()
print(nlist)

# 5.
el = nlist.pop()
print(f"마지막 원소 = {el}")
print(f"nlist = {nlist}")

# 6.
a = ["Life", "is", "too", "short", "you", "need", "python"]
print(a[4], a[2])

# 7.
# for문
b = ["Life", "is", "too", "short"]
str2 = ""
for n in range(len(b)):
    str2 += b[n] + " "

print(str2)

# join함수 위에 결과와 같음
str3 = " ".join(b)
print(str3)

# 8
a = [1, 2, 3]
print(len(a))
# print(a.__sizeof__()) 이건 리스트가 차지하는 메모리 크기를 반환

# 9.
a = [1, 2, 3, 4, 5]
a.pop(1)
a.pop(2)
print(a)

a = [1, 2, 3, 4, 5]
a.remove(2)
a.remove(4)
print(a)


# 파이썬에는 java처럼 contains 함수가 없어서 만들어 줘야 하는거 같음.
# 결국 for문 조건문 사용해서 추출
def filter_by_keyword(lst, keyword):
    return [item for item in lst if keyword in item]


fruits = ["apple", "banana", "grape", "kiwi"]
result = filter_by_keyword(fruits, "a")
print(result)

###############################################
# 튜플 = 내부 값을 변경할 수 없음.
# ex. 좌표(x, y)    rgb(r, g, b) 등등 많이 사용됨

t = 1, 2, 3
print(type(t))

t = 1
print(type(t))

t = 1, ""
print(type(t))

t = (1,)
print(type(t))

t = (1,)
print(type(t))

# t = (, 1) 신택스에러
# print(type(t))

t = "a", "b", ("ab", "cd")
print(t)
print(type(t))

t = (1, 2, 3, 4)
print(t[0])


# 패킹
a = 1, 2
print(a[0])
print(a[1])

# 언패킹
c = 3, 4
d, e = c
print(d)
print(e)

# swap
# 수를 교환하고싶을 때 (ex.최대값 구할 때 등등)

a = 100
b = 200
print(f"swap 이전 : a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"swap 이후 : a = {a}, b = {b}")

# 위와 같지만 아래는 튜플을 이용해서 더 간단하게 함.
a = 100
b = 200
a, b = b, a
print(a, b)

# 튜플도 인덱싱 슬라이싱 가능
t1 = 1, 2, "a", "b"

# '' +, * 연산 가능 list와 같게 동작
# tuple() 튜플로 형변환할 때 리스트를 형변환하면 요소들이 분해되서 튜플로
# 문자열도 분해되서 char마다 튜플로

# in 절로 포함되어 있는지 boolean 가능
print("a" in ("a", "b", "c"))
print("a" in "banana")

# 1부터 100 까지 더한 합을 구하시오.

list1 = list(range(1, 101))
sum = 0
for n in list1:
    sum += n

print(sum)

# 다음의 튜플의 최대값을 구하시오.
tuple1 = 1, 5, 250, 3, 200, 107, 143
max = 0
for n in tuple1:
    if n > max:
        max = n

print(max)

t = 10, 20, 30, 20, 20, 10, 50
print(t.count(10))
print(t.count(20))
print(t.index(30))
print(t.index(50))


# 튜플을 리스트로 변환하여 항목을 변경하고 다시 튜플로 만들어서 출력
t_fruits = "apple", "banana", "water melon"
l_fruits = list(t_fruits)
l_fruits.append("kiwi")
t_fruits = tuple(l_fruits)
print(t_fruits)


# 딕셔너리
# 중복되는 key 사용 x
# key 리스트는 쓸 수 없지만 튜플은 사용 가능(변경가능과 불변의 차이 같음)
person = {"이름": "홍길동", "나이": 26, "몸무게": "75kg"}
person["주소"] = "서울시 마포구 상암로 150"
print(person)

# 키가 없어서 키 에러 발생
# del person['핸드폰번호']
# print(person)

del person["몸무게"]
print(person)

# 인덱스랑 헥갈리면 안됨. dict의 []는 키로 인식
person["직업"] = "율도국의 왕"
print(person)


grade = {"pey": 10, "julliet": 99}
print(grade["pey"])


a = {"name": "pey", "phone": "01199993323", "birth": "1118"}
print(a.keys())

# 다음의 딕셔너리를 키와 밸류를 예쁘게 찍어보자.
dic = {
    "이름": "홍길동",
    "나이": 26,
    "몸무게": 82,
    "직업": "율도국의 왕",
    "주소": "경상북도 울릉군 울릉읍",
}

# dictionary.items 로 (key, value) 의 리스트로 가져와서 찍어봅시다.
dic_items = dic.items()
print(dic_items)

for item in dic_items:
    (key, value) = item
    print(f"{key} : {value}")


lst = [11, 22, 33, 44, 55]
print("pop(0) 이전의 lst[1] :", lst[1])
lst.pop(0)
print("pop(0) 이후 lst[1]:", lst[1])


dic = {0: 11, 1: 22, 2: 33, 3: 44, 4: 55}
print(f"pop(0) 이전 : {dic.items()}")

dic.pop(0)
print(f"pop(0) 이후 : {dic.items()}")

# 문제
a = dict()
print(a)

a["name"] = "python"
a[("a",)] = "python"
# a[[1]] = "python"   TypeError: unhashable type: 'list'
a[250] = "python"
print(a)


a = {"A": 90, "B": 80, "C": 70}
b = a.pop("B")
print(b)

a = {"A": 90, "B": 80, "C": 70}
b = a["B"]
print(b)
del a["B"]
print(a)


a = {"A": 90, "B": 80}
# print(a["C"])     KeyError: 'C'
# print(a.get("C")) 오류는 안나는데 None
print(a.get("C", 70))  # 없으면 디폴트값 70


a = {"A": 90, "B": 80, "C": 70}
values = a.values()
print(values)

min = 100
for i in values:
    if i < min:
        min = i

print(min)


print(list(a.items()))


fruits_dic = {"apple": 6000, "banana": 5000, "orange": 4000}
print(fruits_dic.keys())
print(list(fruits_dic.keys()))

fruits_dic["melon"] = 3000

print(f"fruits_dic 딕셔너리의 항목의 개수 : {len(fruits_dic)}")

print(
    f"{'apple is in fruits_dic' if 'apple' in fruits_dic else "apple isn't in fruits_dic"}"
)
print(
    f"{'mango is in fruits_dic' if 'mango' in fruits_dic else "mango isn't in fruits_dic"}"
)


# set 집합
# 딕셔너리와 비슷하게 생김 {}, 키가 없음

s1 = set([1, 2, 3])
print(s1)
print(type(s1))

# 집합은 중복을 제거하고 순서를 무시(집합은 순서가 중요하지않음)
s2 = set("Hello")
print(s2)

s = set([1, 2, 3])
t = tuple(s)
print(t)

set0 = {}
print(set0)
print(type(set0))  # 는 dict


set0 = set()
print(set0)
print(type(set0))  # 는 set

n_tuple = 1, 2, 3, 4
set2 = set(n_tuple)
print(type(set2))

day_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days_set = set(day_list)
print(days_set)
print(type(days_set))

fruits_tuple = "apple", "orange", "water melon"
print(type(fruits_tuple))
fruits_set = set(fruits_tuple)
print(type(fruits_set))


h_str = "hello"
h_set = set(h_str)
print(h_set)


s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

print(s1 & s2)  # 교집합
print(s1.intersection(s2))

print(s1 | s2)  # 합집합
print(s1.union(s2))

print(s1 - s2)  # 왼쪽을 기준으로 오른쪽과 중복되는걸 제거
print(s1.difference(s2))

print(s1 ^ s2)  # 교집합만 빼고 출력(교집합만 제거)
print()


s1 = {1, 2, 3}
s1.add(4)
print(s1)
# 위 아래 둘 다 추가
s1.update({4, 5, 6})
print(s1)

s1.discard(2)
print(s1)
# 위 아래 둘 다 제거
s1.remove(3)
print(s1)


# 중복허용x 집합 자료형으로
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s = set(a)
print(s)

# s1집합중 s2에 포함된 항목 제거
s1 = set("abced")
s2 = set("cdefg")
print(s1 - s2)

# 비어있는 집합만들기
a = set()
print(a)
print(type(a))

a = set("abc")
a.update(set("def"))
print(a)

# bool
bool("python")  # true
bool("")  # false
bool("     ")  # true
bool([1, 2, 3])  # true
bool([])  # false
bool()  # false
bool(1)  # true
bool(-1)  # true
bool(0)  # false
print(bool(0))

True & False  # false
True | False  # true


# 자동들여쓰기 찾는용
#         grade = {'pey' : 10, 'julliet' : 99}
# print(grade['pey'])

# 번외 이모지를 쓸 수가 있네
# print(f'😎')
# 번외 input은 str 숫자받고싶으면 int()로 형변환(이때 잘 못입력하면 ValueError 발생)
# name = input("이름을 입력해봐\n")
# print(type(name))
# num = int(input("숫자 입력\n"))
# print(type(num))
