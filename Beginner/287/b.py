n, m = map(int, input().split())
s_n = [input() for _ in range(n)]
t_n = [input() for _ in range(m)]

count = 0
for s in s_n:
    end_str = s[-3:]
    if end_str in t_n:
        count += 1
print(count)
