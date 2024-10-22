n, q = map(int, input().split())
ht_q = [input().split() for _ in range(q)]

left, right = 1, 2
cost = 0
for ht in ht_q:
    hand, aim_num = ht[0], int(ht[1])
    if hand == "L":
        if left == aim_num:
            continue
        if left < right < aim_num:
            cost += n - aim_num + left
        elif aim_num < right < left:
            cost += n - left + aim_num
        else:
            cost += abs(left - aim_num)
        left = aim_num
    elif hand == "R":
        if right == aim_num:
            continue
        if right < left < aim_num:
            cost += n - aim_num + right
        elif aim_num < left < right:
            cost += n - right + aim_num
        else:
            cost += abs(right - aim_num)
        right = aim_num
print(cost)
