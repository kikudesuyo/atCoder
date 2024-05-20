n = int(input())
a = []
a_to_c = {}
a_to_idx = {}
for i in range(n):
    a_i, c_i = list(map(int, input().split()))
    a.append(a_i)
    a_to_c[a_i] = c_i
    a_to_idx[a_i] = i + 1

asc_a = sorted(a)

removed_idxes = []
for i in range(n):
    a_i, next_a_i = asc_a[i], asc_a[i + 1]
    if a_to_c[a_i] > a_to_c[next_a_i]:
        removed_idxes.append(a_to_idx[a_i])
    if i == n - 2:
        break


print(n - len(removed_idxes))
for i in range(1, n + 1):
    if i not in removed_idxes:
        print(i, end=" ")
print()
