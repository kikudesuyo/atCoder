n, m = map(int, input().split())

if n == 1:
    print(m + 1)
    exit()

u = n ** (m + 1) - 1
b = n - 1


if b * 10**9 < u:
    print("inf")
else:
    print(u // b)
