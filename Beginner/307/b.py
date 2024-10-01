n = int(input())
s_n = [input() for _ in range(n)]


def is_kaibun(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        string = s_n[i] + s_n[j]
        if is_kaibun(string):
            print("Yes")
            exit()
print("No")
