n = int(input())
a_s = list(map(int, input().split()))
w_s = list(map(int, input().split()))

kind_dict = {}
for i in range(n):
    if not a_s[i] in kind_dict:
        kind_dict[a_s[i]] = [w_s[i]]
    else:
        kind_dict[a_s[i]].append(w_s[i])

result = 0
for values in kind_dict.values():
    temp_sum = sum(values) - max(values)
    result += temp_sum
print(result)
