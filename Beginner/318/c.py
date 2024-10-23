n, d, p = map(int, input().split())
sorted_fn = sorted(list(map(int, input().split())), reverse=True)
total = 0
for i in range(0, n, d):
    tmp_sum = sum(sorted_fn[i : i + d])
    total += min(p, tmp_sum)

print(total)
