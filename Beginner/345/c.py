from collections import defaultdict

s = list(input())

d = defaultdict(int)
for i in range(len(s)):
    d[s[i]] += 1

f = False
for v in d.values():
    if v > 1:
        f = True
        break

if f:
    cnt = 1
else:
    cnt = 0


for char in s:
    sum_num = sum(d.values())
    cnt += sum_num - d[char]
    d[char] -= 1

print(cnt)
