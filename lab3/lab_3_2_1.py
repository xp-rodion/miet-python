def hofstadter_f_m(num: int):
    for value in range(num):
        yield f(value), m(value)


def f(value: int) -> int:
    if value == 0:
        return 1
    return value - m((f(value - 1)))


def m(value: int) -> int:
    if value == 0:
        return 0
    return value - f((m(value - 1)))


for num in hofstadter_f_m(int(input())):
    print(num, end=", ")