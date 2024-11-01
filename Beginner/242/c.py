from collections import defaultdict

n = int(input())

d = defaultdict(int)
for i in range(1, 10):
    d[i] = 1
r = 998244353
for _ in range(n - 1):
    new_d = defaultdict(int)
    for i in range(1, 10):
        if i == 1:
            new_d[1] = (d[1] + d[2]) % r
        elif i == 9:
            new_d[9] = (d[9] + d[8]) % r
        else:
            new_d[i] = (d[i - 1] + d[i] + d[i + 1]) % r
    d = new_d

print(sum(d.values()) % r)
