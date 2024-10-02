n = int(input())
a_n = list(map(int, input().split()))
answers = []
for i in range(n - 1):
    current_num, target_num = a_n[i], a_n[i + 1]
    while target_num != current_num:
        if current_num > target_num:
            answers.append(current_num)
            current_num -= 1

        else:
            answers.append(current_num)
            current_num += 1
answers.append(a_n[-1])
print(*answers)
