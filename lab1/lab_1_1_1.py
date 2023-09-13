def del_virus(s: str, x: str) -> str:
    without_viruses = [symb for symb in s if symb.lower() not in x.lower()]
    return "".join(without_viruses)


print(del_virus(input(), input()))