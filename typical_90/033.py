h, w = map(int, input().split())


if h == 1 or w == 1:
    print(h * w)
    exit()
led_matrix = [[False for _ in range(w)] for _ in range(h)]
initial_on_off = True
for i in range(h):
    for j in range(w):
        if i == 0:
            led_matrix[i][j] = initial_on_off
            initial_on_off = not initial_on_off
            continue
        if j == 0:
            if not led_matrix[i - 1][j]:
                led_matrix[i][j] = True
            continue
        contditions = [
            led_matrix[i - 1][j],
            led_matrix[i][j - 1],
            led_matrix[i - 1][j - 1],
        ]
        if not any(contditions):
            led_matrix[i][j] = True


count = 0
for i in range(h):
    for j in range(w):
        if led_matrix[i][j]:
            count += 1
print(count)
