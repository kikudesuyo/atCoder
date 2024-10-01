a = 998244353
n = int(input())
for i in range(998244353):
    if (n - i) % a == 0:
        print(i)
        break
