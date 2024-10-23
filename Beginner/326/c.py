from bisect import bisect_left

n, m = map(int, input().split())
a_n = list(map(int, input().split()))

sorted_set_a = sorted(list(set(a_n)))

a_dict = {}
for a in sorted_set_a:
    a_dict[a] = 0

for a in a_n:
    a_dict[a] += 1

arr = []
for i in a_dict.values():
    arr.append(i)

cumulatives = [0] * (len(sorted_set_a) + 1)
for i in range(len(sorted_set_a)):
    cumulatives[i + 1] = cumulatives[i] + arr[i]

ans = 0
for i in range(len(sorted_set_a)):
    left_idx = i
    right_idx = bisect_left(sorted_set_a, sorted_set_a[i] + m)
    tmp_diff = cumulatives[right_idx] - cumulatives[left_idx]
    ans = max(ans, tmp_diff)
print(ans)
