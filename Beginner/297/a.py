n, d = map(int, input().split())
t_n = list(map(int, input().split()))


for i in range(n - 1):
    first_click, second_click = t_n[i], t_n[i + 1]
    if second_click - first_click <= d:
        print(second_click)
        exit()
print(-1)
