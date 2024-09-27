n, m, p = map(int, input().split())


count = 0
for i in range(1, n + 1):
    if i % p == m % p:
        count += 1
print(count)
