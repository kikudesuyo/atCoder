q = int(input())
querys = [list(map(int, input().split())) for _ in range(q)]

balls = [0] * 10**6

ball_kind_count = 0
for query in querys:
    balls = [0] * 10**6
    if query[0] == 3:
        print(ball_kind_count)
        continue
    num, x = query
    if num == 1:
        if balls[x - 1] == 0:
            ball_kind_count += 1
        balls[x - 1] += 1
    elif num == 2:
        if balls[x - 1] == 1:
            ball_kind_count -= 1
        balls[x - 1] -= 1
