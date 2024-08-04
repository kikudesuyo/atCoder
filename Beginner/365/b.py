n = int(input())
a_s = list(map(int, input().split()))


sorted_a = sorted(a_s, reverse=True)

second_num = sorted_a[1]

print(a_s.index(second_num) + 1)
