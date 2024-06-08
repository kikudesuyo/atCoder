# n = int(input())

# v_n = [n * (10**i) for i in range(n)]
# sum = 0
# for i in range(n):
#     sum += v_n[i] % 998244353
# sum = sum % 998244353
# print(sum)
n = input()
sum = n * (1 - 10 ** len(n))
