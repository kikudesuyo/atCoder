from itertools import chain, combinations

a, b, c, d, e = map(int, input().split())

arr = [("A", a), ("B", b), ("C", c), ("D", d), ("E", e)]
c = list(chain.from_iterable(combinations(arr, r) for r in range(len(arr) + 1)))

ans = sorted(c, key=lambda x: (-sum([y[1] for y in x]), [y[0] for y in x]))


for e in ans:
    t = []
    for i in e:
        t.append(i[0])
    print("".join(t))
