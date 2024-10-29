from collections import defaultdict

n = int(input())
fs_n = [list(map(int, input().split())) for _ in range(n)]

ices = defaultdict(list)
for i in range(n):
    f, s = fs_n[i]
    ices[f].append(s)

same_max = 0
for f, vals in ices.items():
    if len(vals) >= 2:
        vals.sort(reverse=True)
        yam = vals[0] + vals[1] // 2
        same_max = max(same_max, yam)

top_arr = []
for f, vals in ices.items():
    top_arr.append(max(vals))
if len(top_arr) <= 1:
    print(same_max)
    exit()

sorted_top_arr = sorted(top_arr, reverse=True)
diff_max = sorted_top_arr[0] + sorted_top_arr[1]
if same_max > diff_max:
    print(same_max)
else:
    print(diff_max)
