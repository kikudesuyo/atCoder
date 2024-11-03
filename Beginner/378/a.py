a_n = list(map(int, input().split()))
set_a = set(a_n)


if len(set_a) == 4:
    print(0)
if len(set_a) == 3:
    print(1)
if len(set_a) == 2:
    if a_n.count(a_n[0]) == 2:
        print(2)
    else:
        print(1)
if len(set_a) == 1:
    print(2)
