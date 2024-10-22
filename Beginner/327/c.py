a_nn = [list(map(int, input().split())) for _ in range(9)]
matrix_a = list(zip(*a_nn))

for row in matrix_a:  # aの列を確認
    if len(set(row)) != 9:
        print("No")
        exit()
for row in a_nn:  # aの行を確認
    if len(set(row)) != 9:
        print("No")
        exit()

dict_a = {}
for i in range(3):
    for j in range(3):
        dict_a[(i, j)] = []


for i in range(9):
    for j in range(9):
        dict_a[(i // 3, j // 3)].append(a_nn[i][j])

for elem in dict_a.values():  # aの3x3のマスを確認
    if len(set(elem)) != 9:
        print("No")
        exit()
print("Yes")
