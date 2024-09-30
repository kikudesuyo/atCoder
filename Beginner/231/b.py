n = int(input())
s_n = [input() for _ in range(n)]

candates = list(set(s_n))

max_count = 0
answer = ""
for candate in candates:
    if max_count <= s_n.count(candate):
        answer = candate
        max_count = max(max_count, s_n.count(candate))
print(answer)
