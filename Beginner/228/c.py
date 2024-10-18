from bisect import bisect_right

n, k = map(int, input().split())
p_n = [sum(list(map(int, input().split()))) for _ in range(n)]

sorted_p_n = sorted(p_n)

for i in range(n):
    idx = bisect_right(sorted_p_n, p_n[i] + 300)
    rank = n - idx + 1
    if rank <= k:
        print("Yes")
    else:
        print("No")
