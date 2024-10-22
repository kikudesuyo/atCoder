n, c = map(int, input().split())
t_n = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
count = 1
sec = t_n[0]
for i in range(1, n):
    if t_n[i] - sec >= c:
        count += 1
        sec = t_n[i]
print(count)
