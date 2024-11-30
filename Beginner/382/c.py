from bisect import bisect_right

n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_m = list(map(int, input().split()))

aa = []
min_num = 10**9
for i in range(n):
    if a_n[i] < min_num:
        min_num = a_n[i]
        aa.append((i, a_n[i]))

aa.reverse()

key_aa = [a[1] for a in aa]

for i in range(m):
    idx = bisect_right(key_aa, b_m[i])
    if idx == 0:
        print(-1)
    else:
        print(aa[idx - 1][0] + 1)
