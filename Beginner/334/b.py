# URL: https://atcoder.jp/contests/abc334/tasks/abc334_b
# 切り捨てと切り上げについての問題
a, m, l, r = map(int, input().split())
# leftは切り上げ, rightは切り捨て
left, right = (l - a + m - 1) // m, (r - a) // m
print(max(0, right - left + 1))
