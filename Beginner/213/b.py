n = int(input())
a_n = list(map(int, input().split()))

sorted_a_n = sorted(a_n)
num = sorted_a_n[-2]
print(a_n.index(num) + 1)
