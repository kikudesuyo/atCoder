n = int(input())
s = input()


for i in range(1, n):
    idx = 0
    temp = 0
    for j in range(n):
        if i + j >= n:
            print(j)
            break
        if s[j] == s[i + j]:
            print(j)
            break
