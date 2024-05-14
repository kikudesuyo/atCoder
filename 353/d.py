# 数学的に式の意味を理解して分解するのが今回のポイントだった。また、共通のものがある場合は、増えていくようにループを回すと良さそう。
n = int(input())
a_s = list(map(int, input().split()))
divided_num = 998244353
# str(a)+str(b)のstr(b)の部分を考える
right_total = 0
for j in range(1, n):
    right_total += a_s[j] * j
# str(a)+str(b)のstr(a)の部分を考える
mutiple_num = 0
left_total = 0
for i in reversed(range(n)):
    mutiple_num += 10 ** len(str(a_s[i]))
    left_total += a_s[i - 1] * mutiple_num
    if i == 1:
        break


print((right_total + left_total) % divided_num)
