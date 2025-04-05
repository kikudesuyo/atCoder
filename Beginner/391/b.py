n, m = map(int, input().split())
s_nn = [list(input()) for _ in range(n)]
t_mm = [list(input()) for _ in range(m)]


for s_row in range(n - m + 1):
    for s_column in range(n - m + 1):
        flag = True
        val = (s_row, s_column)
        for t_row in range(m):
            for t_column in range(m):
                if (
                    not s_nn[s_row + t_row][s_column + t_column]
                    == t_mm[t_row][t_column]
                ):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(s_row + 1, s_column + 1)
            exit()
