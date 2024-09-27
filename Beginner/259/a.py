n, m, x, t, d = map(int, input().split())


baby_tall = t - (d * x)

for i in range(n + 1):
    if i == 0:
        talls = [baby_tall]
        temp = baby_tall
        continue
    if i <= x:
        temp += d
    talls.append(temp)


print(talls[m])
