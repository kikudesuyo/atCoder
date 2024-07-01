from bisect import bisect_left, bisect_right

n, t = map(int, input().split())
s = input()
x_s = list(map(int, input().split()))

left_directions = []
right_directions = []

for i in range(n):
    if s[i] == "0":
        left_directions.append(x_s[i])
    else:
        right_directions.append(x_s[i])

left_sorted = sorted(left_directions)
right_sorted = sorted(right_directions)

count = 0
for pos in left_sorted:
    min_range = pos - 2 * t
    max_range = pos
    # 入るべき位置をそれぞれ探して、間の数を数える
    right_idx = bisect_right(right_sorted, max_range)
    left_idx = bisect_left(right_sorted, min_range)
    count += right_idx - left_idx

print(count)
