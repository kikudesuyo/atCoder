from itertools import combinations

n, m = map(int, input().split())

kx = [list(map(int, input().split())) for _ in range(m)]

combination_num = n * (n - 1) // 2

array = []
for i in range(m):
    k_i, x_arr = kx[i][0], kx[i][1:]
    x_combinatins = list(combinations(x_arr, 2))
    array += x_combinatins


if len(set(array)) == combination_num:
    print("Yes")
else:
    print("No")
