# 반복


class EvenCounter:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        t = self.n
        self.n = t + 2
        return t


my_even = EvenCounter()
# print(my_even.__next__())
# print(my_even.__next__())
# print(my_even.__next__())
# print(my_even.__next__())

for i in range(5):
    print(my_even.__next__())


# 클래스 EvenNumber 만들기
# 클래스에는 n이라는 속성이 있다. 짝수 하나 있는 것
# 객체를 0을 가진 것 하나, 2를 가진 것하나, ....20을 가진 객체를 만들어서
# 이를 리스트에 넣고 이 리스트를 0,2,4,6,8,....20 출력


class EvenNumber:
    def __init__(self, n):
        self.n = n

    def getN(self):
        return self.n


listn = list()

for i in range(0, 21, 2):
    listn.append(EvenNumber(i))

for i in listn:
    print(i.getN(), end=" ")


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


print()
l1 = [1, 2, 3, 4]
l2 = [0, 2, 4, 8]
l3 = [0, 0, 0, 0]
print(all(l1))
print(all(l2))
print(all(l3))
# all() = 모두가 참이여야 true
# any() = 하나라도 참이면 true
# bool() = 빈칸도 true 값이 있다면 true


time_str = "25-04-07 09:49:20"
t1 = time_str.split()

# 천단위 쉼표 출력 금액 출력할 때 좋음
print("{:,}".format(123345346))

print("위도: {0}, 경도: {1}".format("35.17N", "129.07E"))
print("위도 : {lat}, 경도 : {long}".format(lat="3517N", long="129.07E"))


user_input = input("숫자를 입력해주세요. ")
input_list = user_input.split(",")
sum = 0
for num in input_list:
    sum += int(num)

print(f"{user_input}의 총합은 {sum} 입니다.")
