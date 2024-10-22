from itertools import combinations

n = list(input())

first = []
for i in range(1, (len(n) // 2) + 1):
    first = first + list(combinations(n, i))


def rest(all, first):
    second = all.copy()
    for item in first:
        if item in second:
            second.remove(item)
    return second


splits = {}
for i in range(len(first)):
    second_i = rest(n, first[i])
    splits[i] = {"first": first[i], "second": second_i}


max = 0
for i in range(len(splits)):
    first = sorted(splits[i]["first"], reverse=True)
    second = sorted(splits[i]["second"], reverse=True)
    if first[0] == "0" or second[0] == "0":
        continue
    int_first, int_second = int("".join(first)), int("".join(second))
    if int_first * int_second > max:
        max = int_first * int_second
print(max)
