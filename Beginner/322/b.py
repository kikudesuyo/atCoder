n, m = map(int, input().split())
s = input()
t = input()
count = 3
# 接尾辞か?
if s == t[-n:]:
    count -= 1
# 接頭辞か?
if s == t[:n]:
    count -= 2
print(count)
