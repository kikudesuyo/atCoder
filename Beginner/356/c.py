import itertools

n, m, k = map(int, input().split())


c_s = []
a_s = []
r_s = []
for i in range(m):
    elem = input().split()
    c_s.append(int(elem[0]))
    a_s.append(list(map(int, elem[1:-1])))
    r_s.append(elem[-1])


def b_s(a_s, length):
    return [i for i in range(1, length + 1) if i not in a_s]


candidates = []
for pair in itertools.combinations(range(1, n + 1), k):
    candidates.append(pair)

removed_candidates = []

for i in range(m):
    if r_s[i] == "o":
        for candidate in candidates:
            for c in candidate:
                if c not in a_s[i]:
                    removed_candidates.append(candidate)
                    break
    else:
        for candidate in candidates:
            if all(j in candidate for j in a_s[i]):
                removed_candidates.append(candidate)


set_removed_candidate = list(map(list, set(map(tuple, removed_candidates))))
print(len(candidates) - len(set_removed_candidate))
