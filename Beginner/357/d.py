str_n = input()
int_n = int(str_n)

p = 998244353


# 繰り返し二乗法を使用していない
# numerator = (10 ** (int_n * len(str_n)) - 1) % p
# denominator = (10 ** len(str_n) - 1) % p

# 繰り返し二乗法を使用しているコード
numerator = pow(10, int_n * len(str_n), p) - 1
denominator = pow(10, len(str_n), p) - 1

# 分母の逆元を取って計算する
ans = (int_n * numerator * pow(denominator, -1, p)) % p

print(ans)
