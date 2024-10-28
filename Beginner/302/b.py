h, w = map(int, input().split())
s_h = [list(input()) for _ in range(h)]


def check_width_snuke(arr, h):
    snuke = "snuke"
    reversed_snuke = "ekuns"
    for i in range(h):
        if snuke in "".join(arr[i]):
            s_idx = "".join(arr[i]).index("snuke")
            return [
                (i + 1, s_idx + 1),
                (i + 1, s_idx + 2),
                (i + 1, s_idx + 3),
                (i + 1, s_idx + 4),
                (i + 1, s_idx + 5),
            ]
        if reversed_snuke in "".join(arr[i]):
            e_idx = "".join(arr[i]).index("ekuns")
            return [
                (i + 1, e_idx + 5),
                (i + 1, e_idx + 4),
                (i + 1, e_idx + 3),
                (i + 1, e_idx + 2),
                (i + 1, e_idx + 1),
            ]
    return []


def check_height_snuke(s_h, h, w):
    snuke = "snuke"
    reversed_snuke = "ekuns"
    ans = []
    for i in range(h - 4):
        for j in range(w):
            if s_h[i][j] == "s":
                for k in range(5):
                    if snuke[k] == s_h[i + k][j]:
                        ans.append((i + k + 1, j + 1))
                    else:
                        ans = []
                        break
                    if k == 4:
                        return ans
            if s_h[i][j] == "e":
                for k in range(5):
                    if reversed_snuke[k] == s_h[i + k][j]:
                        ans.append((i + k + 1, j + 1))
                    else:
                        ans = []
                        break
                    if k == 4:
                        return sorted(ans, reverse=True)
    return []


def check_diagonal_snuke(s_h, h, w):
    snuke = "snuke"
    reversed_snuke = "ekuns"
    ans = []
    r, c = 0, 0
    while True:  # 左上から右下
        if c + 4 == w:
            c = 0
            r += 1
        if r + 4 == h:
            break
        if s_h[r][c] == "s":
            for i in range(5):
                if s_h[r + i][c + i] == snuke[i]:
                    ans.append((r + i + 1, c + i + 1))
                else:
                    ans = []
                    break
                if i == 4:
                    return ans
        if s_h[r][c] == "e":
            for i in range(5):
                if s_h[r + i][c + i] == reversed_snuke[i]:
                    ans.append((r + i + 1, c + i + 1))
                else:
                    ans = []
                    break
                if i == 4:
                    return sorted(ans, reverse=True)
        c += 1

    snuke = "snuke"
    reversed_snuke = "ekuns"
    ans = []
    c, r = 4, 0
    while True:  # 右上から左下
        if c == w:
            c = 4
            r += 1
        if r + 4 == h:
            return []
        if s_h[r][c] == "s":
            for i in range(5):
                if s_h[r + i][c - i] == snuke[i]:
                    ans.append((r + i + 1, c - i + 1))
                else:
                    ans = []
                    break
                if i == 4:
                    return ans
        if s_h[r][c] == "e":
            for i in range(5):
                if s_h[r + i][c - i] == reversed_snuke[i]:
                    ans.append((r + i + 1, c - i + 1))
                else:
                    ans = []
                    break
                if i == 4:
                    return sorted(ans, reverse=True)
        c += 1


width = check_width_snuke(s_h, h)
if width:
    for i in width:
        print(*i)
    exit()
height = check_height_snuke(s_h, h, w)
if height:
    for i in height:
        print(*i)
    exit()
diagonal = check_diagonal_snuke(s_h, h, w)
if diagonal:
    for i in diagonal:
        print(*i)
    exit()
