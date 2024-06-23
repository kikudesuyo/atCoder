s_x, s_y = map(int, input().split())
t_x, t_y = map(int, input().split())
# 左側に寄せる
if s_y % 2 == 0:
    if s_x % 2 == 0:
        left_s_x = s_x
    else:
        left_s_x = s_x - 1
else:
    if s_x % 2 == 0:
        left_s_x = s_x - 1
    else:
        left_s_x = s_x
if t_y % 2 == 0:
    if t_x % 2 == 0:
        left_t_x = t_x
    else:
        left_t_x = t_x - 1
else:
    if t_x % 2 == 0:
        left_t_x = t_x - 1
    else:
        left_t_x = t_x

# 左に移動
if left_s_x > left_t_x:
    y_diff = abs(s_y - t_y)
    # 上下移動だけですむ場合
    if left_s_x - left_t_x <= y_diff:
        print(y_diff)
    else:
        x_count = ((left_s_x - left_t_x) - y_diff) // 2
        print(y_diff + x_count)
# 右に移動
else:
    y_diff = abs(s_y - t_y)
    # 上下移動だけですむ場合
    if left_t_x - left_s_x <= y_diff + 1:
        print(y_diff)
    else:
        x_count = ((left_t_x - left_s_x) - (y_diff + 1)) // 2
        print(y_diff + 1 + x_count)
