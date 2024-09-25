n = int(input())
a_n = list(map(int, input().split()))

answers = []
for i in a_n:
    if i % 2 == 0:
        answers.append(i)
print(*answers)
