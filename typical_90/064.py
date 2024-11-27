# 解説AC
# 地殻変動で変化するのは左右の端だけであることを利用する
# 参考文献: https://sugizakkworld.com/593/


n, q = map(int, input().split())
a_n = list(map(int, input().split()))
lrv_q = [list(map(int, input().split())) for _ in range(q)]

diff = [0] * (n - 1)
for i in range(n - 1):
    diff[i] = a_n[i + 1] - a_n[i]
result = sum(map(abs, diff))

for query in range(q):
    l, r, v = lrv_q[query]
    l -= 1
    r -= 1

    if l != 0:  # 左側の変化を更新
        result -= abs(diff[l - 1])
        diff[l - 1] += v
        result += abs(diff[l - 1])
    if r != n - 1:
        result -= abs(diff[r])
        diff[r] -= v
        result += abs(diff[r])
    print(result)
