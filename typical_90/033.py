h, w = map(int, input().split())

count = 0
if h == 1 or w == 1:
    # 条件を満たしていないので全て点灯させてOK
    count = h * w
else:
    for i in range(h):
        for j in range(w):
            if i % 2 == 0 and j % 2 == 0:
                count += 1
print(count)
