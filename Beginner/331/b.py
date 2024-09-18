n, s, m, l = map(int, input().split())


min_money = 1000000000000000000000
for i in range(0, 100):
    for j in range(0, 100):
        for k in range(0, 100):
            if i * 6 + j * 8 + k * 12 >= n:
                money = i * s + j * m + k * l
                if money < min_money:
                    min_money = money

print(min_money)
