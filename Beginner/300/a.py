n, a, b = map(int, input().split())
c_n = list(map(int, input().split()))

print(c_n.index(a + b) + 1)
