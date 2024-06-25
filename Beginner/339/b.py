h, w, n = map(int, input().split())

grid = [["."] * w for _ in range(h)]

row, column = 0, 0
up, down, left, right = False, False, False, True

# 移動方向を決めてgridに記入
for i in range(n):
    if i == 0:
        grid[row][column] = "#"
        continue
    if right:
        column = 0 if column == w - 1 else column + 1
    elif down:
        row = 0 if row == h - 1 else row + 1
    elif left:
        column = w - 1 if column == 0 else column - 1
    elif up:
        row = h - 1 if row == 0 else row - 1
    # まだ記入されていない場合は記入して時計回りに移動
    if grid[row][column] == ".":
        grid[row][column] = "#"
        if right:
            right, down = False, True
        elif down:
            down, left = False, True
        elif left:
            left, up = False, True
        elif up:
            up, right = False, True
    # すでに記入されている場合は元に戻して反時計回りに移動
    else:
        grid[row][column] = "."
        if right:
            right, up = False, True
        elif down:
            down, right = False, True
        elif left:
            left, down = False, True
        elif up:
            up, left = False, True

# gridを出力
for i in range(h):
    print("".join(grid[i]))
