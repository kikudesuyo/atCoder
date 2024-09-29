# ライブラリを使用すると非常に大きい数字のときにエラーになる。

n = int(input())
bin_n = bin(n)[2:]
print(len(bin_n) - 1)
