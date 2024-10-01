s = input()


def is_kaibun(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


max_num = 0
for i in range(len(s)):
    for j in range(len(s)):
        if i > j:
            continue
        string = s[i : j + 1]
        if is_kaibun(string):
            max_num = max(len(string), max_num)

print(max_num)
