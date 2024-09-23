a, b = map(int, input().split())

min_num, max_num = min(a, b), max(a, b)

if min_num in [1, 3]:
    if max_num in [2]:
        print("Yes")
    else:
        print("No")
if min_num in [2]:
    if max_num in [1, 3]:
        print("Yes")
    else:
        print("No")
if min_num in [4, 6]:
    if max_num in [5]:
        print("Yes")
    else:
        print("No")
if min_num in [5]:
    if max_num in [4, 6]:
        print("Yes")
    else:
        print("No")
if min_num in [7, 9]:
    if max_num in [8]:
        print("Yes")
    else:
        print("No")
if min_num in [8]:
    if max_num in [7, 9]:
        print("Yes")
    else:
        print("No")
