n = int(input())
a_n = list(map(int, input().split()))

a = 0
for i in range(n):
    if i % 2 == 0:
        a += a_n[i]
print(a)
