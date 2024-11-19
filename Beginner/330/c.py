import math

d = int(input())


sqrt_x = math.isqrt(d)
if sqrt_x**2 != d:
    sqrt_x += 1


diff = 10**12
sqrt_j = 0
for sqrt_i in reversed(range(1, sqrt_x + 1)):
    while True:
        diff = min(diff, abs(sqrt_i * sqrt_i + sqrt_j * sqrt_j - d))
        if sqrt_i**2 + sqrt_j**2 > d:
            break
        sqrt_j += 1
print(diff)
