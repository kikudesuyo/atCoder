n = int(input())
cp_n = []
for i in range(n):
    cp_n.append(list(map(int, input().split())))

q = int(input())
lr_q = []
for i in range(q):
    lr_q.append(list(map(int, input().split())))


cumulative_1 = [0] * n
cumulative_2 = [0] * n

temp_class_1_sum, temp_class_2_sum = 0, 0
for idx in range(len(cp_n)):
    c_i, p_i = cp_n[idx]
    if c_i == 1:
        temp_class_1_sum += p_i
        cumulative_1[idx] = temp_class_1_sum
        cumulative_2[idx] = temp_class_2_sum
    else:
        temp_class_2_sum += p_i
        cumulative_1[idx] = temp_class_1_sum
        cumulative_2[idx] = temp_class_2_sum


for l, r in lr_q:
    l_idx, r_idx = l - 1, r - 1
    if l_idx == 0:
        sum_class_1 = cumulative_1[r_idx]
        sum_class_2 = cumulative_2[r_idx]
    else:
        sum_class_1 = cumulative_1[r_idx] - cumulative_1[l_idx - 1]
        sum_class_2 = cumulative_2[r_idx] - cumulative_2[l_idx - 1]
    print(sum_class_1, sum_class_2)
