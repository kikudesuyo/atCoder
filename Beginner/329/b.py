n = int(input())
a_s = list(map(int, input().split()))

sorted_a_s = sorted(a_s, reverse=True)
max_a = sorted_a_s[0]
for i in sorted_a_s:
    if i != max_a:
        print(i)
        exit()
