from collections import defaultdict
from itertools import combinations


def same_nums(list_a, list_b):
    return list(set(list_a) & set(list_b))


n = int(input())


d = {}
num_dicts = []
for i in range(n):
    ipt = list(map(int, input().split()))
    d[i] = (ipt[0], ipt[1:])
    n_d = defaultdict(int)
    for i in ipt[1:]:
        n_d[i] += 1
    num_dicts.append(n_d)


combs = list(combinations(d.keys(), 2))

max_num = 0
for key_1, key_2 in combs:
    val_1, val_2 = d[key_1], d[key_2]
    t = 0
    for i in same_nums(val_1[1], val_2[1]):
        dict_1, dict_2 = num_dicts[key_1], num_dicts[key_2]
        t += (dict_1[i] / val_1[0]) * (dict_2[i] / val_2[0])
    max_num = max(max_num, t)

print(max_num)
