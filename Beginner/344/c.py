n = int(input())
a_s = list(map(int, input().split()))
m = int(input())
b_s = list(map(int, input().split()))
l = int(input())
c_n = list(map(int, input().split()))
q = int(input())
x_s = list(map(int, input().split()))

comb_sum = set([])
for a in a_s:
    for b in b_s:
        for c in c_n:
            comb_sum.add(a + b + c)
for x in x_s:
    if x in comb_sum:
        print("Yes")
    else:
        print("No")
