a_n = list(map(int, input().split()))

num = 0
for i in range(len(a_n)):
    num += a_n[i] * 2**i
print(num)
