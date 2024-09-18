n, s, k = map(int, input().split())

sum_num = 0
for i in range(n):
    p, q = map(int, input().split())
    sum_num += p * q
if sum_num < s:
    sum_num += k

print(sum_num)
