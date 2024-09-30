n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

for i in range(m):
    pasta_length = b_n[i]
    if not pasta_length in a_n:
        print("No")
        exit()
    idx = a_n.index(pasta_length)
    a_n.pop(idx)
print("Yes")
