a, b, c, d, e, f = map(int, input().split())
div = 998244353
print(((a * b * c) - (d * e * f)) % div)
