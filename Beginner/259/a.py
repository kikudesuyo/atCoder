n, m, x, t, d = map(int, input().split())


tall = t
for i in range(m):
    if i == x:
        break
    tall += d
print(tall)
