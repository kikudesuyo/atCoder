p_n = list(map(int, input().split()))
alphabets = "abcdefghijklmnopqrstuvwxyz"

answer = ""
for i in p_n:
    answer += alphabets[i - 1]
print(answer)
