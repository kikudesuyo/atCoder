from collections import defaultdict

n = int(input())
a_nn = [list(map(int, list(input()))) for _ in range(n)]


def c(cur_r, cur_c, a_nn):
    n_length = len(a_nn)
    ans = ""
    # 左上
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r - i, cur_c - i, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 上
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r, cur_c - i, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 右上
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r + i, cur_c - i, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 左
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r - i, cur_c, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 右
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r + i, cur_c, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 左下
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r - i, cur_c + i, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 下
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r, cur_c + i, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    # 右下
    tmp = ""
    for i in range(n_length):
        r, c = change(cur_r + i, cur_c + i, n_length)
        tmp += str((a_nn[r][c]))
    ans = max(ans, tmp)
    return ans


def change(r, w, n):
    return r % n, w % n


d = defaultdict(list)
for i in range(n):
    for j in range(n):
        d[a_nn[i][j]].append((i, j))
max_num = max(d.keys())
start_idxes = d[max_num]

ans = ""
for row, col in start_idxes:
    ans = max(ans, c(row, col, a_nn))
print(ans)
