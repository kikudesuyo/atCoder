n = int(input())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

answer_1 = 0
answer_2 = 0

for i in range(n):
    if a_n[i] == b_n[i]:
        answer_1 += 1
    else:
        if a_n[i] in b_n:
            answer_2 += 1
print(answer_1)
print(answer_2)
