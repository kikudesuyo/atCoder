n = int(input())


def carpet(cur_carpet, cur_level):
    arr = []
    for i in range(3**cur_level):
        arr.append(cur_carpet[i] * 3)
    for i in range(3**cur_level):
        arr.append(cur_carpet[i] + ["."] * 3**cur_level + cur_carpet[i])
    for i in range(3**cur_level):
        arr.append(cur_carpet[i] * 3)
    return arr


level1 = [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]

if n == 0:
    print("#")
    exit()
elif n == 1:
    for elems in level1:
        print("".join(elems))
    exit()

cur_carpet = level1
for i in range(1, n):
    arr = carpet(cur_carpet, i)
    cur_carpet = arr


for elems in cur_carpet:
    print("".join(elems))
