n, q = map(int, input().split())
l_nn = [list(map(int, input().split())) for _ in range(n)]
st_qq = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    s, t = st_qq[i]
    print(l_nn[s - 1][t])
