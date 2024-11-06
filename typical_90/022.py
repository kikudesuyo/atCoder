import math

a, b, c = map(int, input().split())
min_unit = math.gcd(a, b, c)
ans = (a - 1) // min_unit + (b - 1) // min_unit + (c - 1) // min_unit
print(ans)
