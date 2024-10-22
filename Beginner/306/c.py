n = int(input())
a_3n = list(map(int, input().split()))

set_a = set(a_3n)
a_dict = {}
for a in set_a:
    a_dict[a] = []


for idx in range(len(a_3n)):
    a_dict[a_3n[idx]].append(idx + 1)

ans_dict = {}
for idx in range(len(a_dict.keys())):
    ans_dict[a_dict[idx + 1][1]] = idx + 1

sorted_ans_dict = dict(sorted(ans_dict.items()))
print(*sorted_ans_dict.values())
