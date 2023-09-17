lst = list(map(int, input().split()))
dyn_lst = lst[:]
k = 0

for _ in lst:
    if 0 not in dyn_lst:
        dyn_lst = [num - 1 for num in dyn_lst]
        k += 1
        continue

lst = dyn_lst[:]

while True:

    if not [num for num in lst if num > 0]:
        break

    border = []
    for index, num in enumerate(lst):
        if num > 0:
            border.append(index)
            continue

        if not border:
            continue
        break

    if not border:
        continue

    left, right = border[0], None if border[-1] + 1 == len(lst) else border[-1] + 1
    dyn_lst = lst[left:right]
    minimum = min(dyn_lst)
    dyn_lst = [num - minimum for num in dyn_lst]
    lst[left:right] = dyn_lst
    k += minimum

print("Мин-ое кол-во шагов: ", k)