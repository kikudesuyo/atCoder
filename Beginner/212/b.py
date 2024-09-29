hoge = input()
passwords = int(hoge[0]), int(hoge[1]), int(hoge[2]), int(hoge[3])

if len(set(passwords)) == 1:
    print("Weak")
    exit()


current_num = passwords[0]
for i in range(1, 4):
    if current_num == 9 and passwords[i] == 0:
        current_num = 0
    elif current_num + 1 == passwords[i]:
        current_num = passwords[i]
    else:
        print("Strong")
        exit()

print("Weak")
