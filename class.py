#
#
#

# class


class Counter:
    # current = 0 이랑 같은 거임
    def __init__(self, stop):
        # self(자기자신).current(current라는 변수를) 0으로 선언
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current = r + 1
            return r
        else:  # 없으니까 무한루프...
            raise StopIteration


for i in Counter(3):
    print(i, end=" ")
