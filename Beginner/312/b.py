n, m = map(int, input().split())
s_n = [list(input()) for _ in range(n)]


tak_code = []
for i in range(9):
    row = []
    for j in range(9):
        if i <= 2 and j <= 2:
            row.append("#")
        elif i == 3 and j <= 3:
            row.append(".")
        elif j == 3 and i <= 3:
            row.append(".")
        elif i == 5 and j >= 5:
            row.append(".")
        elif j == 5 and i >= 5:
            row.append(".")
        elif i >= 6 and j >= 6:
            row.append("#")

        else:
            row.append("-")
    tak_code.append(row)


def sn_block(s_n, i, j):
    block = []
    for k in range(9):
        block.append(s_n[i + k][j : j + 9])
    return block


for i in range(n - 8):
    for j in range(m - 8):
        flag = True
        s_n_block = sn_block(s_n, i, j)
        for r_idx in range(9):
            for c_idx in range(9):
                if tak_code[r_idx][c_idx] == "-":
                    continue
                if tak_code[r_idx][c_idx] != s_n_block[r_idx][c_idx]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(i + 1, j + 1)
