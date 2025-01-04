x = int(input())

arr = [[0] * 9 for i in range(9)]

for i in range(9):
    for j in range(9):
        arr[i][j] = (i + 1) * (j + 1)

cnt = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] != x:
            cnt += arr[i][j]
print(cnt)
