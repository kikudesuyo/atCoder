n = int(input())
ab_n = [list(map(int, input().split())) for _ in range(n)]

total_time = 0
for a, b in ab_n:
    total_time += a / b

# 左からtota_time//2秒の距離を算出
time = 0
i = 0
distance = 0
while time * 2 <= total_time:
    time += ab_n[i][0] / ab_n[i][1]
    distance += ab_n[i][0]
    i += 1

if time * 2 == total_time:
    print(time)
    exit()
else:
    i -= 1
    time -= ab_n[i][0] / ab_n[i][1]
    distance -= ab_n[i][0]


diff_time = total_time / 2 - time
print(distance + ab_n[i][1] * diff_time)
