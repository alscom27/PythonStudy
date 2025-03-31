# # print("hahahaha")

# print("대한민국은 사계절이 뚜렷한 나라입니다.")

x = 20

if x>=20 :
    print("x는 20보다 크거나 같다.")
else :
    print("x는 20보다 작다.")


# 제곱은 **
a = 4
a2 = a**0.5
print(a)
print(a2)

# 반지름을 넣고 원의 둘레와 면적을 구해봅시다.
radius = 4
cc = 2*3.14*radius
area = 3.14*radius**2
print("원의 반지름은",radius,"입니다.", sep="")
print("원의 둘레는 ", cc, " 입니다.", sep="")
print("원의 면적은 ", area, " 입니다.")
print("원의 면적은{}입니다.".format(area))

print('나의 이름은 :', '홍길동')
print('나의 나이는 :', 27)
print('나의 키는', 179, 'cm입니다.')
print('10 + 20 = ', 10+20)

# 2 가지 정도 변수 명을 만드는 컨벤션(관습)
# 카멜 케이스(자바 계열 많이 쓰는 방식) ex. thanksGivingDay
# 스네일 케이스(파이썬 계열 많이 쓰는 방식) ex. thanks_giving_day

# 배열 일 때 복수명을 쓸거냐?
name = ["이승권", "홍길동", "이순신", "나영석"]
names = ["이승권", "홍길동", "이순신", "나영석"]
nameList = ["이승권", "홍길동", "이순신", "나영석"]
name_list = ["이승권", "홍길동", "이순신", "나영석"]

name_t = ("이승권", "홍길동")
name_s = {"이승권", "홍길동"}
name_d = {"이승권" : "홍길동"}

print(name.__class__)
print(name_t.__class__)
print(name_s.__class__)
print(name_d.__class__)

str1 = "123"
print(str1)
print(str1.__add__("456"))
print(str1)
str1 = "456"
str1[0].__add__("456")
print(str1[0].__add__("456"))
print(str1)
print(str1[0:1], str1[0:1])
print(str1[0:1], "5")
print(str1)
str2 = '5' + str1[1:]
print(str2)

print(name_d.keys())

print(type(name_d))

a = 10
a += 5
print(a)

a = 10
b = '177'
c = a + int(b)
print("c = a + b :", c)

d = 'abc'
e = 222
f = d + str(e)
print("f = d + e :", f)

print("="*40)
print(124 * 456)
print(1357 + 2468)
print(5 ** 4)
print(10 / 4)
print(10 // 5)
print(10 % 5)
print("="*40)
print( 5 % 2)
print(2 ** 0.5)
print(3 ** 0.5)
print("="*40)

num_a, num_b = 100, 200

print(num_a == num_b)
print(num_a != num_b)
print(num_a > num_b)
print(num_a < num_b)
print(num_a >= num_b)
print("false" == "false")
print((num_a > num_b) & (num_b < num_a))
print((num_a > num_b) | True)

print("="*40)
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool(500))
print(bool(''))
print(bool('str'))
print("="*40)

a = False
b = a | True == True
print(b)
# a = True
b = a & False == False
print(b)

print("="*40)
a = True
b = False
c = not(a | b)
print(c)
d = (not a) | (not b)
print(d)
e = (not a) & (not b)
print(e)
# c = e

print("="*40)
k_score = 80
e_score = 75
m_score = 55

print("홍길동 씨의 평균 점수는 {}점 입니다.".format((k_score + e_score + m_score)/3))

num = 13
if(num % 2 == 0) :
    print("짝수입니다.")
else :
    print("홀수입니다.")
    
# 파이썬에서 3항연산자? 사용법
# true 조건문 else
print("짝수입니다." if num % 2 == 0 else "홀수입니다.")