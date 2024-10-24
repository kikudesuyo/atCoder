from bisect import bisect_right

n = int(input())
a_n = list(map(int, input().split()))

set_an = sorted(list(set(a_n)))


cnt_s = {}
for i in range(n):
    cnt_s[i] = 0
for i in range(n):
    a_i = a_n[i]
    idx = bisect_right(set_an, a_i)
    cnt_s[len(set_an) - idx] += 1


for i in cnt_s.values():
    print(i)
