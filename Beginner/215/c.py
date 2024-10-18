from itertools import permutations

s, str_k = input().split()
k = int(str_k)
s = list(s)

p = set(list(permutations(s, len(s))))
combi = []
for i in p:
    combi.append("".join(i))
sorted_combi = sorted(combi)
print(sorted_combi[k - 1])
