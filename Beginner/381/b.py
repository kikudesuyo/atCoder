from collections import defaultdict

s = list(input())

if len(s) % 2 == 1:
    print("No")
    exit()

for i in range(0, len(s), 2):
    if s[i] != s[i + 1]:
        print("No")
        exit()

d = defaultdict(int)
for i in s:
    d[i] += 1

for i in d.values():
    if i != 2:
        print("No")
        exit()
print("Yes")
