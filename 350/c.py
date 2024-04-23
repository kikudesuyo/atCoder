n = int(input())
array = list(map(int, input().split()))

dict = {}
for idx, elem in enumerate(array):
    dict[elem] = idx


sorted_elems = []
for i in range(n):
    if array[i] == i + 1:
        continue
    # ここがポイント。1個ずつ変えて参照すると、変更後の値を参照してしまいうまく変更することが出来ない。
    # 配列と辞書の変更によって依存しないようなコードを書くことで、混乱が避けられそう。
    # うまく分離しよう
    j = dict[i + 1]
    dict[array[i]], dict[array[j]] = dict[array[j]], dict[array[i]]
    array[i], array[j] = array[j], array[i]
    sorted_elems.append([i + 1, j + 1])

print(len(sorted_elems))
if len(sorted_elems) != 0:
    for elem in sorted_elems:
        print(f"{elem[0]} {elem[1]}")
