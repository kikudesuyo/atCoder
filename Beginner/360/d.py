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


def find_smaller_or_equal_numbers(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    # スライスの計算量はO(k)なので、今回は不適切
    return arr[:left]


def find_larger_numbers(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # スライスの計算量はO(k)なので、今回は不適切
    return arr[left:]


count = 0
for i in range(len(left_sorted)):
    min_range = left_sorted[i] - 2 * t
    max_range = left_sorted[i]
    partial_right_directions = find_smaller_or_equal_numbers(right_sorted, max_range)
    partial_left_directions = find_larger_numbers(partial_right_directions, min_range)
    count += len(partial_left_directions)
print(count)
