n = int(input())
array = list(map(int, input().split()))

dict = {}
for idx, elem in enumerate(array):
    dict[elem] = idx


sorted_elems = []
for i in range(n):
    if array[i] == i + 1:
        continue
    j = dict[i + 1]
    dict[array[i]], dict[array[j]] = dict[array[j]], dict[array[i]]
    array[i], array[j] = array[j], array[i]
    sorted_elems.append([i + 1, j + 1])

print(len(sorted_elems))
if len(sorted_elems) != 0:
    for elem in sorted_elems:
        print(f"{elem[0]} {elem[1]}")
