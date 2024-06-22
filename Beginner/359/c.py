s_x, s_y = map(int, input().split())
t_x, t_y = map(int, input().split())
# 左側に寄せる
if s_y % 2 == 0:
    if s_x % 2 == 0:
        even_s_x = s_x
    else:
        even_s_x = s_x - 1
else:
    if s_x % 2 == 0:
        even_s_x = s_x - 1
    else:
        even_s_x = s_x
if t_y % 2 == 0:
    if t_x % 2 == 0:
        even_t_x = t_x
    else:
        even_t_x = t_x - 1
else:
    if t_x % 2 == 0:
        even_t_x = t_x - 1
    else:
        even_t_x = t_x


# 左に移動
if even_s_x > even_t_x:
    y_diff = abs(s_y - t_y)
    # 上下移動だけですむ場合
    if even_s_x - even_t_x <= y_diff:
        print(y_diff)
    else:
        x_count = ((even_s_x - even_t_x) - y_diff) // 2
        print(y_diff + x_count)
# 右に移動
else:
    y_diff = abs(s_y - t_y)
    # 上下移動だけですむ場合
    if even_t_x - even_s_x <= y_diff + 1:
        print(y_diff)
    else:
        x_count = ((even_t_x - even_s_x) - (y_diff + 1)) // 2
        print(y_diff + 1 + x_count)
