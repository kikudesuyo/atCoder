n = int(input())
a_n = list(map(int, input().split()))

set_a_n = set(a_n)

a_dict = {}
for a_elem in set_a_n:
    a_dict[a_elem] = 0

for a_elem in a_n:
    a_dict[a_elem] += 1

count = 0
for a_elem in a_dict.values():
    count += a_elem // 2
print(count)
