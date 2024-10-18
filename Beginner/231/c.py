from bisect import bisect_left

n, q = map(int, input().split())
a_n = list(map(int, input().split()))
x_q = [int(input()) for _ in range(q)]

sorted_an = sorted(a_n)
for query in x_q:
    idx = bisect_left(sorted_an, query)
    print(n - idx)
