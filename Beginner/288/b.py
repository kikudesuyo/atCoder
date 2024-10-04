n, k = map(int, input().split())
s_n = [input() for _ in range(n)]
sorted_s_n = sorted(s_n[:k])
for i in sorted_s_n:
    print(i)
