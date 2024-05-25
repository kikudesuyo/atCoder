n, m = list(map(int, input().split()))
a_s = list(map(int, input().split()))
b_s = list(map(int, input().split()))

all = a_s + b_s

all_sorted = sorted(all)


flag = False
for idx in range(len(all_sorted)):
    if flag:
        if all_sorted[idx] in a_s:
            print("Yes")
            exit()
    if all_sorted[idx] in a_s:
        flag = True
    else:
        flag = False

print("No")
