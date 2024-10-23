from itertools import permutations

n, m = map(int, input().split())
s_n = [input() for _ in range(n)]

all = list(permutations(s_n, n))

for elems in all:
    flag = True
    for idx in range(len(elems) - 1):
        left, right = elems[idx], elems[idx + 1]
        cnt = 0
        for i in range(m):
            if left[i] == right[i]:
                cnt += 1
        if cnt != m - 1:
            flag = False
    if flag:
        print("Yes")
        exit()
print("No")
