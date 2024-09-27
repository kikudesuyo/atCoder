list = list(map(int, input().split()))
b = list[1]

sorted_list = sorted(list)
if sorted_list[1] == b:
    print("Yes")
else:
    print("No")
