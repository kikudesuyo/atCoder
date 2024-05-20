n = int(input())
a = []
a_to_c = {}
a_to_idx = {}
for i in range(n):
    a_i, c_i = list(map(int, input().split()))
    a.append(a_i)
    a_to_c[a_i] = c_i
    a_to_idx[a_i] = i

asc_a = sorted(a)

seletcted_idxes = [(a_to_idx[asc_a[-1]])]

i = n - 1
j = n - 2
while j >= 0:
    if a_to_c[asc_a[j]] < a_to_c[asc_a[i]]:
        seletcted_idxes.append(a_to_idx[asc_a[j]])
        i = j
    j -= 1

print(len(seletcted_idxes))
for idx in sorted(seletcted_idxes):
    print(idx + 1, end=" ")
print()
