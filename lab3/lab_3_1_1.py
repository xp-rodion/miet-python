def reducer(ch: int, zn: int) -> tuple:
    if len([num for num in (ch, zn) if num % 2 == 0]) != 2:
        return int(ch), int(zn)
    return reducer(ch / 2, zn / 2)


print(reducer(int(input()), int(input())))