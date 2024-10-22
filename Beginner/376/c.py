n = int(input())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

sorted_a_n = sorted(a_n, reverse=True)
sorted_b_n = sorted(b_n, reverse=True)

box_idx = 0
tmp = []
try:
    for i in range(n):
        toy = sorted_a_n[i]
        current_box = sorted_b_n[box_idx]
        if current_box >= toy:
            box_idx += 1
        else:
            tmp.append(toy)
except:
    print(min(sorted_a_n))
    exit()

if len(tmp) == 1:
    print(tmp[0])
    exit()
else:
    print(-1)
    exit()
