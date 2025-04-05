from itertools import combinations

a_n = list(map(int, input().split()))

s = sorted(a_n)

for i in range(len(a_n) - 1):
    a_n[i], a_n[i + 1] = a_n[i + 1], a_n[i]
    if a_n == s:
        print("Yes")
        exit()
    a_n[i], a_n[i + 1] = a_n[i + 1], a_n[i]

print("No")
