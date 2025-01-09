n = int(input())
x_s, y_s = [], []
for _ in range(n):
    x, y = map(int, input().split())
    x_s.append(x)
    y_s.append(y)

x_s.sort()
y_s.sort()

cnt = 0
x = x_s[n // 2]
y = y_s[n // 2]
for i in range(n):
    cnt += abs(x - x_s[i]) + abs(y - y_s[i])
print(cnt)
