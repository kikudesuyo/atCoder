from collections import defaultdict

n = int(input())
xy_n = [list(map(int, input().split())) for _ in range(n)]
s = list(input())

d = defaultdict(lambda: {"L": [], "R": []})
for i in range(n):
    x, y = xy_n[i]
    if s[i] == "L":
        d[y]["L"].append(x)
    elif s[i] == "R":
        d[y]["R"].append(x)


for _, v in d.items():
    if len(v["L"]) > 0 and len(v["R"]) > 0:
        if max(v["L"]) > min(v["R"]):
            print("Yes")
            exit()
print("No")
