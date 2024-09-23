n, x = map(int, input().split())
a_s = list(map(int, input().split()))

min_num = 101
for j in range(101):
    arr = a_s.copy()
    arr.append(j)
    sum_num = sum(arr) - (min(arr) + max(arr))
    if sum_num >= x:
        min_num = min(min_num, j)

if min_num == 101:
    print(-1)
else:
    print(min_num)
