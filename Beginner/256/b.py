n = int(input())
a_n = list(map(int, input().split()))


balls = []
p = 0
for i in range(n):
    balls.append(0)
    balls = [ball + a_n[i] for ball in balls]
    temp = []
    for ball in balls:
        if ball <= 3:
            temp.append(ball)
        else:
            p += 1
    balls = temp

print(p)
