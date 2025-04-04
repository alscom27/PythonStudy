#
#
#


# 가변인자를 받을 때는 *붙이기
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def sum_mul(choice, *args):

    if choice == "sum":
        result = 0
        for i in args:
            result += i

    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


result = sum_mul("sum", 1, 2, 3, 4, 5)
print(result)
result = sum_mul("mul", 1, 2, 3, 4, 5)
print(result)


def sum_nums(*numbers):
    sum = 0
    for n in numbers:
        sum += n

    avg = sum / len(numbers)
    result = f"합계 : {sum}, 평균 : {avg}"
    print(result)


sum_nums(1, 2, 3, 4, 5)


#  *args(Tuple)  **kwargs(Dict)
def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, name="foo", age=3)


def func(*data, **method):
    num = sum(data) * method["scale"]  # num = 120
    print(num, method["unit"] + "입니다.")


func(3, 4, 5, scale=10, unit="개")
