n, d = map(int, input().split())
s_n = [input() for _ in range(n)]

max_num = 0
flag = False
days = 0
for j in range(d):
    for i in range(n):
        if s_n[i][j] != "o":
            flag = True
            break
    if not flag:
        days += 1
    else:
        flag = False
        days = 0
    max_num = max(max_num, days)
print(max_num)
