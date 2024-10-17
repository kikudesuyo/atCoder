n, m = map(int, input().split())
a_m = list(map(int, input().split()))

day = 1
idx = 0
for i in range(n):
    print(a_m[idx] - day)
    if a_m[idx] == day:
        idx += 1
    day += 1
