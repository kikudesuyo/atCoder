s = input()

list_s = list(s)

if len(list(set(list_s))) == 3:
    print(list_s[0])
elif len(list(set(list_s))) == 2:
    for i in list_s:
        if not list_s.count(i) == 2:
            print(i)
            break

else:
    print("-1")
