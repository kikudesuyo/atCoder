h, m = map(int, input().split())

# 見間違えない条件
# Aが2のときかつCが5以上
# Bが6以上

# 23:59までの時刻を全探索
for hour in range(h, 24):
    for minute in range(60):
        if h == hour and m > minute:
            continue
        if hour % 10 >= 6:
            continue
        if hour // 10 >= 2:
            if minute // 10 >= 4:
                continue
        print(hour, minute)
        exit()

# 先の条件で一致しなかった場合、0:00からh-1:59までの時刻を全探索
for hour in range(0, h + 1):
    for minute in range(60):
        if h == hour and m < minute:
            continue
        if hour % 10 >= 6:
            continue
        if hour // 10 >= 2:
            if minute // 10 >= 4:
                continue
        print(hour, minute)
        exit()
