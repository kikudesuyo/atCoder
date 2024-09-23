n = int(input())
a_s = list(map(int, input().split()))

is_same = True
init_num = a_s[0]
for i in a_s:
    if i != init_num:
        is_same = False
        break
if is_same:
    print("Yes")
else:
    print("No")
