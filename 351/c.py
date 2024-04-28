n = int(input())
a_s = list(map(int, input().split()))
idx = 0
while True:
    if idx == len(a_s) - 1:
        print(len(a_s))
        exit()
    if len(a_s) == 1:
        continue
    if a_s[idx] != a_s[idx + 1]:
        idx += 1
    elif a_s[idx] == a_s[idx + 1]:
        insert_num = a_s.pop(idx) + 1
        a_s.pop(idx)
        a_s.insert(idx, insert_num)
        idx += -1
        if idx < 0:
            idx = 0
