class OddCounter:
    def __init__(self, n=1):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        t = self.n
        self.n += 2
        return t

    # def __next__(self):
    #     t = self.n
    #     self.n += 2
    #     if t < 20 :
    #         return t
    #     else: # 반복끝내기
    #         raise StopIteration


my_counter = OddCounter()
# print(next(my_counter))
# print(my_counter.__next__())
# print(my_counter.__next__())
# print(my_counter.__next__())
print()

for x in my_counter:
    if x > 20:
        break
    print(x, end=" ")

# for i in my_counter:
#     print(i, end=" ")
