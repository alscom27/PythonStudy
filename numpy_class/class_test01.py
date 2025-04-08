class User:
    phone_number = ""
    email_address = ""
    name = ""

    # 초기 initalize 함수 => 생성자
    def init(self, phone_number, email_address, name):
        self.phone_number = phone_number
        self.email_address = email_address
        self.name = name

    def getPhoneNumber(self):
        return self.phone_number

    def getEmail(self):
        return self.email_address

    def getName(self):
        return self.name


user1 = User()
user1.init("010-1234-5678", "kjs@naver.com", "김준선")
print(user1.getPhoneNumber())
print(user1.getEmail())
print(user1.getName())


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second


# a = FourCal()
# # a.setdata(4, 2)
# # print(a.first, a.second)
# FourCal.setdata(a, 7, 8)
# print(a.first)
# print(a.second)


# class FourCal:
#     count = 0

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def sum(self):
#         result = self.first = self.second
#         FourCal.count += 1
#         return result


# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# print(a.first, a.second)
# print(a.sum())

# print(FourCal().count)

# b = FourCal()
# b.setdata(7, 8)
# print(b.sum())
# print(FourCal().count)


class Daeheeyun:
    class_value = 0

    def __init__(self):
        self.instance_value = 0

    def set_class_value(self):
        Daeheeyun.class_value = 10

    def set_intance_value(self):
        self.class_value = 20


instance1 = Daeheeyun()
instance2 = Daeheeyun()

print("...클래스 속성 변경...")
instance1.set_class_value()
print(instance1.class_value, instance2.class_value)

print("... 인스턴스 속성 변경...")
instance1.set_intance_value()
print(instance1.class_value, instance2.class_value)


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result


# 클래스 상속
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first**self.second
#         return result


# m = MoreFourCal(FourCal(4, 2))
# print(m.pow())
# print(m.sum())
# print(m.first)


class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Scientific_Calculator(Calculator):
    pass


# class BaseClass:
#     def myfunc(self):
#         print("Base c f")


# class InhClass(BaseClass):
#     def myfunc(self):
#         print("inh c f")


# ex1 = BaseClass()
# ex1.myfunc()
# ex2 = InhClass()
# ex2.myfunc()


class Base1:
    def myfunc(self):
        print("base1")


class Base2:
    member1 = 100
    member2 = 200


class Base3:
    def myfunc2(self, a, b):
        print(a + b)


class InhClass(Base1, Base2, Base3):
    member3 = 300


ex1 = InhClass()
ex1.myfunc()
ex1.myfunc2(ex1.member1, ex1.member3)


class A:
    def greeting(self):
        print("안녕하세요 . A 입니다.")


class B(A):
    def greeting(self):
        print("안녕하세요. B 입니다.")


class C(A):
    def greeting(self):
        print("안녕하세요. C 입니다.")


class D(B, C):
    pass


x = D()
x.greeting()

# mro() 어떤 순서로 돌았는지 보여줌
print(D.mro())


class Person:
    def greeting(self):
        print("안녕하세요.")


class Student(Person):
    def greeting(self):
        super().greeting()
        print("저는 파이썬 코딩 도장 학생입니다.")


tom = Person()
tom.greeting()
james = Student()
james.greeting()


class Data:
    def __init__(self, data):
        tmp = data.split("|")
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]

    def print_age(self):
        print(self.age)

    def print_grade(self):
        print(f"{self.name}님 당신의 점수는 {self.grade} 입니다.")


data = Data("홍길동|42|A")
data.print_age()
data.print_grade()
