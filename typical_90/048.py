n, k = map(int, input().split())
ab_n = [list(map(int, input().split())) for _ in range(n)]


arr = []
for a, b in ab_n:
    arr.append(b)
    arr.append(a - b)

b_arr = sorted(arr, reverse=True)

print(sum(b_arr[:k]))
