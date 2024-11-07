n = int(input())
array = list(map(int, input().split()))


val_to_idx = {}
for i in range(n):
    val_to_idx[array[i]] = i

answers = []
for i in range(n):
    if array[i] == i + 1:
        continue
    cur_num = i + 1
    cur_idx = val_to_idx[cur_num]
    target_num = array[i]
    array[cur_idx] = target_num
    array[i] = i + 1

    val_to_idx[cur_num] = i
    val_to_idx[target_num] = cur_idx
    answers.append((i + 1, cur_idx + 1))

print(len(answers))
for answer in answers:
    print(answer[0], answer[1])
