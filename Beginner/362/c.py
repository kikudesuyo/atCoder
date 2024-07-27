n = int(input())
lr_s = []
min_count, max_count = 0, 0
only_plus_min_count, only_minus_max_count = 0, 0
for i in range(n):
    l, r = map(int, input().split())
    lr_s.append([l, r])
    if l > 0:
        only_plus_min_count += l
    elif r < 0:
        only_minus_max_count += r
    min_count += l
    max_count += r


if min_count > 0 or max_count < 0:
    print("No")
    exit()


# プラスに偏ってるなら正、マイナスに偏ってるなら負
diff = only_plus_min_count + only_minus_max_count
output_strings = []
left_diff = diff
for l, r in lr_s:

    if l > 0:
        output_strings.append(l)
    elif r < 0:
        output_strings.append(r)
    # 0を堺にしているためlは負の値、rは正の値(l,rはゼロになりうる)
    else:
        if left_diff == 0:
            output_strings.append(0)
        # プラスのほうが多いとき
        elif diff > 0:
            # まだまだ差分があるとき
            if left_diff > abs(l):
                output_strings.append(l)
                left_diff += l
            else:
                output_strings.append(-left_diff)
                left_diff = 0
        # マイナスのほうが多いとき
        elif diff < 0:
            # まだまだ差分があるとき
            if abs(left_diff) > r:
                output_strings.append(r)
                left_diff += r
            else:
                output_strings.append(-left_diff)
                left_diff = 0
        else:
            output_strings.append(0)


print("Yes")
print(*output_strings)
