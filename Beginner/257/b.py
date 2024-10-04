n, k, q = map(int, input().split())
a_k = list(map(int, input().split()))
l_q = list(map(int, input().split()))

for i in range(q):
    if l_q[i] == k:
        if a_k[l_q[i] - 1] == n:
            pass
        else:
            a_k[l_q[i] - 1] += 1
    elif a_k[l_q[i] - 1] + 1 == a_k[l_q[i]]:
        pass
    else:
        a_k[l_q[i] - 1] += 1
print(*a_k)
