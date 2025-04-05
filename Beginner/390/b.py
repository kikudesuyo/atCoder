from math import gcd

n = int(input())
a_n = list(map(int, input().split()))


ratios = []

for i in range(1, n):
    a = a_n[i]
    b = a_n[i - 1]
    c = gcd(a, b)
    ratios.append((a // c, b // c))

if len(set(ratios)) == 1:
    print("Yes")
    exit()

print("No")
