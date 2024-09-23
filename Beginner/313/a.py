n = int(input())
p_s = list(map(int, input().split()))
me = p_s[0]
soreted_p_s = sorted(p_s, reverse=True)
if n == 1:
    print(0)
    exit()
second = soreted_p_s[1]
if me == second:
    print(1)
elif max(p_s) == p_s[0]:
    print(0)
else:
    print(max(p_s) - p_s[0] + 1)
