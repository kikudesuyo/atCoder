n, r = map(int, input().split())
da_n = [list(map(int, input().split())) for _ in range(n)]

current_rate = r
for d, a in da_n:
    if d == 1:
        if 1600 <= current_rate <= 2799:
            current_rate += a
    elif d == 2:
        if 1200 <= current_rate <= 2399:
            current_rate += a

print(current_rate)
