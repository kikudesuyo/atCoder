import math
from collections import defaultdict
from itertools import combinations_with_replacement

n, m = map(int, input().split())


def combi_w_re(n, m):
    return math.comb(n + m - 1, m)


default_nums = [0] * n
for i in range(n):
    default_nums[i] = 1 + 10 * i
diff = m - default_nums[-1]
arr = [i for i in range(n)]
t = diff
ans = []

while True:
    if t < 0:
        break
    else:
        combinations = list(combinations_with_replacement(arr, t))
        for combi in combinations:
            temp_nums = default_nums.copy()
            d = defaultdict(int)
            for num in combi:
                d[num] += 1
            s = 0
            for i in range(n):
                if i in d.keys():
                    s += d[i]
                temp_nums[i] += s
            ans.append(temp_nums)
        t -= 1

length = 0
for i in range(diff + 1):
    length += combi_w_re(n, i)
print(length)

ans = sorted(ans)
for a in ans:
    print(*a)
