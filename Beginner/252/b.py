n, k = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

max_num = max(a_n)
max_idxes = [i + 1 for i, a in enumerate(a_n) if a == max_num]

for i in range(k):
    if b_n[i] in max_idxes:
        print("Yes")
        exit()
print("No")
