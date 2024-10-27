n, x, y, z = map(int, input().split())
math_n = list(map(int, input().split()))
eng_n = list(map(int, input().split()))
sum_n = [x + y for x, y in zip(math_n, eng_n)]

math_dict = {}
for i in range(n):
    if math_n[i] in math_dict:
        math_dict[math_n[i]].append(i)
    else:
        math_dict[math_n[i]] = [i]

eng_dict = {}
for i in range(n):
    if eng_n[i] in eng_dict:
        eng_dict[eng_n[i]].append(i)
    else:
        eng_dict[eng_n[i]] = [i]

sum_dict = {}
for i in range(n):
    if sum_n[i] in sum_dict:
        sum_dict[sum_n[i]].append(i)
    else:
        sum_dict[sum_n[i]] = [i]
pass_list = []
rest = x
sorted_maths = sorted(math_dict.items(), key=lambda x: -x[0])
for key, idxes in sorted_maths:
    for idx in idxes:
        if rest == 0:
            break
        pass_list.append(idx)
        rest -= 1
rest = y
sorted_engs = sorted(eng_dict.items(), key=lambda x: -x[0])
for key, idxes in sorted_engs:
    for idx in idxes:
        if rest == 0:
            break
        if idx not in pass_list:
            pass_list.append(idx)
            rest -= 1

rest = z
sorted_sums = sorted(sum_dict.items(), key=lambda x: -x[0])
for key, idxes in sorted_sums:
    for idx in idxes:
        if rest == 0:
            break
        if idx not in pass_list:
            pass_list.append(idx)
            rest -= 1

sorted_pass_list = sorted(pass_list)

for i in sorted_pass_list:
    print(i + 1)
