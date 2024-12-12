n = int(input())
a_n = list(map(int, input().split()))

total = sum(a_n)

means = [total // n] * n
if total == sum(means):
    pass
else:
    diff = total - sum(means)
    for i in range(diff):
        means[i] += 1

means.sort()
a_n.sort()

minus_cnt = 0
plus_cnt = 0
for i in range(n):
    if means[i] < a_n[i]:
        minus_cnt += a_n[i] - means[i]
    elif means[i] > a_n[i]:
        plus_cnt += means[i] - a_n[i]

print(minus_cnt)
