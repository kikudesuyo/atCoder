from itertools import combinations

n = int(input())
k_n = list(map(int, input().split()))

# Maxが最小ということはMinが最大
results = []
sum_num = sum(k_n)
for i in range(1, len(k_n) - 1):
    for conb in combinations(k_n, i):
        results.append(conb)

if results == []:
    print(min(k_n))
    exit()

min_a = sum_num
for result in results:
    raw_1, raw_2 = sum(result), sum_num - sum(result)
    a, b = max(raw_1, raw_2), min(raw_1, raw_2)
    if a < min_a:
        min_a = min(a, min_a)
print(min_a)
