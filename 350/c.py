n = int(input())
array = list(map(int, input().split()))

# n = 3
# array = [3, 1, 2]
# n = 5
# array = [3, 4, 1, 2, 5]
sort_elems = []
num = 1


for idx in range(n):
    if array[idx] > num:
        sort_elems.append([num, array.index(num) + 1])
        # 右側のインデックスを変化
        array[array.index(num)] = array[idx]
        # 左側のインデックスを変化
        array[idx] = num
    num += 1

# print(sort_elems)

print(len(sort_elems))
if len(sort_elems) != 0:
    for elem in sort_elems:
        print(f"{elem[0]} {elem[1]}")
