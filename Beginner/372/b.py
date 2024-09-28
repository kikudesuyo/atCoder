m = int(input())


reminder = m
answers = []
num = 10
while reminder != 0:
    if reminder > (3**num):
        answers.append(num)
        reminder -= 3**num
    # if reminder // (3**num) == 0:
    else:
        num -= 1

print(len(answers))
print(*answers)
