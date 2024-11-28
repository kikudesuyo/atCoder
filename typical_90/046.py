from collections import defaultdict

n = int(input())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))
c_n = list(map(int, input().split()))

p = 46

a_d = defaultdict(int)
b_d = defaultdict(int)
c_d = defaultdict(int)
for a in a_n:
    a_d[a % p] += 1
for b in b_n:
    b_d[b % p] += 1
for c in c_n:
    c_d[c % p] += 1

cnt = 0
for i in range(p):
    for j in range(p):
        for k in range(p):
            if (i + j + k) % p == 0:
                cnt += a_d[i] * b_d[j] * c_d[k]

print(cnt)
