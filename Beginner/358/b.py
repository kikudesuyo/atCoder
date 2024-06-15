n, a = map(int, input().split())

t_s = list(map(int, input().split()))

time_count = 0
t_idx = 0
while True:
    if t_idx == n:
        break
    if time_count >= t_s[t_idx]:
        time_count += a
        print(time_count)
        t_idx += 1
        continue
    time_count += 1
