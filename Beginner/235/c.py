from collections import defaultdict

n, q = map(int, input().split())
a_n = list(map(int, input().split()))
xk_q = [list(map(int, input().split())) for _ in range(q)]


a_dict = defaultdict(list)
for idx, elem in enumerate(a_n):
    a_dict[elem].append(idx)

for x, k in xk_q:
    if a_dict[x]:
        if len(a_dict[x]) < k:
            print(-1)
        else:
            print(a_dict[x][k - 1] + 1)
    else:
        print(-1)
