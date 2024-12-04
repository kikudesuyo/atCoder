from collections import defaultdict

n, k = map(int, input().split())
a_n = list(map(int, input().split()))

sorted_a_n = sorted(a_n)

d = defaultdict(list)
for i in range(k):
    cnt = 0
    idx = i + cnt * k
    while idx < n:
        d[i].append((idx, a_n[idx]))
        cnt += 1
        idx = i + cnt * k


swap_arr = [0] * n
for i in range(k):
    idx_sort = sorted([x[0] for x in d[i]])
    val_sort = sorted([x[1] for x in d[i]])
    for j in range(len(d[i])):
        swap_arr[idx_sort[j]] = val_sort[j]

if sorted_a_n == swap_arr:
    print("Yes")
else:
    print("No")
