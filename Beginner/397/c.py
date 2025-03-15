from collections import defaultdict

n = int(input())
a_n = list(map(int, input().split()))


d = defaultdict(int)

for i in range(n):
    d[a_n[i]] += 1

first = set()
first.add(a_n[0])
d[a_n[0]] -= 1
second = set()
for i in range(1, n):
    second.add(a_n[i])


max_num = len(first) + len(second)

for i in range(1, n - 1):
    first.add(a_n[i])
    if d[a_n[i]] == 1:
        second.remove(a_n[i])
    else:
        d[a_n[i]] -= 1
    max_num = max(max_num, len(first) + len(second))
print(max_num)
