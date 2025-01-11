n, d = map(int, input().split())
tl_n = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, d + 1):
    max_num = 0
    for j in range(n):
        multh = tl_n[j][0] * (tl_n[j][1] + i)
        max_num = max(max_num, multh)
    print(max_num)
