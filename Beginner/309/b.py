n = int(input())
a_nn = [list(map(int, list(input()))) for _ in range(n)]

b_nn = [[-1] * n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n - 1 or col == n - 1:
            if row == 0:
                if col == n - 1:
                    b_nn[row + 1][col] = a_nn[row][col]
                else:
                    b_nn[row][col + 1] = a_nn[row][col]
            elif row == n - 1:
                if col == 0:
                    b_nn[row - 1][col] = a_nn[row][col]
                else:
                    b_nn[row][col - 1] = a_nn[row][col]
            elif col == 0:
                # row=0, n-1のときは上で処理
                b_nn[row - 1][col] = a_nn[row][col]
            elif col == n - 1:
                # row=0, n-1のときは上で処理
                b_nn[row + 1][col] = a_nn[row][col]
        else:
            b_nn[row][col] = a_nn[row][col]
            continue

for row in b_nn:
    print("".join(map(str, row)))
