def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더 할 수 있는 것이 아닙니다.")
    else:
        return a + b
