n = int(input())
h_n = list(map(int, input().split()))

max_num = max(h_n)
print(h_n.index(max_num) + 1)
