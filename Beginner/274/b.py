h, w = map(int, input().split())
c_hw = [input() for _ in range(h)]
tranposition = [[c_hw[i][j] for i in range(h)] for j in range(w)]
ans = []
for i in range(w):
    ans.append(tranposition[i].count("#"))
print(*ans)
