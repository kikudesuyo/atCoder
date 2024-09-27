n, p, q = map(int, input().split())
d_s = list(map(int, input().split()))

min_meal = min(d_s)

if min_meal + q <= p:
    print(min_meal + q)
else:
    print(p)
