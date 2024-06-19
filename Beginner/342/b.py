n = int(input())
p_s = list(map(int, input().split()))
q = int(input())
a_b_s = []
for i in range(q):
    a_b_s.append(list(map(int, input().split())))

for i in range(q):
    first_idx, second_idx = p_s.index(a_b_s[i][0]), p_s.index(a_b_s[i][1])
    if first_idx < second_idx:
        print(a_b_s[i][0])
    else:
        print(a_b_s[i][1])
