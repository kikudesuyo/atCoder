from itertools import combinations

n, m = map(int, input().split())
c_n = []
a_n = []
for i in range(m):
    c_n.append(input())
    a_n.append(list(map(int, input().split())))

cnt = 0


for i in range(1, m + 1):
    for c in combinations(range(m), i):
        arr = [False] * n
        for c_i in c:
            for e in a_n[c_i]:
                arr[e - 1] = True
        if arr.count(True) == n:
            cnt += 1

print(cnt)
