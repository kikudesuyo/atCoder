n = int(input())
a_s = list(map(int, input().split()))
a_dict = {}
for idx in range(n):
    a_dict[idx] = a_s[idx]
check_a = []
input_count = 0
reverse_flag = False
while input_count < n + 1:
    if reverse_flag:
        if len(check_a) < 2:
            reverse_flag = False
            continue
        if check_a[-1] == check_a[-2]:
            check_a.pop()
            check_a[-1] += 1
            continue
    if input_count == n:
        break
    if len(check_a) == 0:
        check_a.append(a_dict[input_count])
        input_count += 1
        continue
    if check_a[-1] == a_dict[input_count]:
        check_a[-1] += 1
        input_count += 1
        reverse_flag = True
    elif check_a[-1] != a_dict[input_count]:
        check_a.append(a_dict[input_count])
        input_count += 1

print(len(check_a))
