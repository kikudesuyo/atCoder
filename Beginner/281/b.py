s = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if len(s) < 8:
    print("No")
    exit()
first = s[0]
second = s[1:-1]
last = s[-1]
if first in alphabet and last in alphabet:
    try:
        int(second)
    except:
        print("No")
        exit()
    if 100000 <= int(second) <= 999999:
        if second[0] == "0":
            print("No")
            exit()
        print("Yes")
        exit()
print("No")
