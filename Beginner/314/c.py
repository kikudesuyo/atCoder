from collections import defaultdict

n, m = map(int, input().split())
s = list(input())
c_n = list(map(int, input().split()))

d_c = defaultdict(list)
for i in range(n):
    d_c[c_n[i]].append(i)

init_d_c = d_c.copy()

for i in range(1, m + 1):
    arr = d_c[i]
    shifted_arr = [arr[-1]] + arr[:-1]
    d_c[i] = shifted_arr


ans = [""] * n
for key, value in d_c.items():
    for i in range(len(value)):
        ans[init_d_c[key][i]] = s[value[i]]

print("".join(ans))
