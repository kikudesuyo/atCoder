n, x, y = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

sorted_a_n = sorted(a_n, reverse=True)
sorted_b_n = sorted(b_n, reverse=True)

x_count, y_count = 0, 0
for i in range(n):
    x_count += sorted_a_n[i]
    y_count += sorted_b_n[i]
    if x_count > x or y_count > y:
        print(i + 1)
        exit()

print(n)
