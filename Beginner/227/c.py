# 解説AC: ルートの状況を使わずに累乗の形で考える
# ルートで計算すると少数が発生するため丸め誤差が発生して厄介

n = int(input())

cnt = 0
for i in range(1, n + 1):
    if i**3 > n:
        break
    for j in range(i, n + 1):
        if i * (j**2) > n:
            break
        cnt += n // (i * j) - j + 1
print(cnt)
