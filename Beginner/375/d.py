s = input()

set_s = set(s)
dict = {}

for i in set_s:
    dict[i] = []


for i in range(len(s)):
    dict[s[i]].append(i)


def sum_line(n):
    return n * (n - 1) // 2


answer = 0
for arr in dict.values():
    if len(arr) < 2:
        pass
    temp = 0
    head = -1 * (len(arr) - 1)
    for elem in arr:
        temp += head * elem
        head += 2
    answer += temp - sum_line(len(arr))
print(answer)
