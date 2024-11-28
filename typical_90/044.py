n, q = map(int, input().split())
a_n = list(map(int, input().split()))
txy_q = [list(map(int, input().split())) for _ in range(q)]

shift_num = 0
for t, x, y in txy_q:
    i_1 = (x - 1 - shift_num) % n
    i_2 = (y - 1 - shift_num) % n
    if t == 1:
        a_x, a_y = a_n[i_1], a_n[i_2]
        a_n[i_1], a_n[i_2] = a_y, a_x
    elif t == 2:
        shift_num += 1
        shift_num %= n
    elif t == 3:
        print(a_n[x - 1 - shift_num])
