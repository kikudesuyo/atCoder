from collections import defaultdict

k = int(input())


d = defaultdict(list)

arr = []
for i in range(1, 10):  # 1桁
    arr.append(i)

d[1] = arr

for i in range(1, 10):  # 2桁
    for j in range(10):
        if i > j:
            d[2].append(i * 10 + j)


for i in range(3, 11):  # 3桁以上
    previous_arr = d[i - 1]
    for elem in previous_arr:
        for j in range(int(str(elem)[0]) + 1, 10):
            d[i].append(j * 10 ** (i - 1) + elem)

arr = []
for i in range(1, 11):
    arr.extend(sorted(d[i]))

print(arr[k - 1])
