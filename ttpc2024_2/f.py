q = int(input())
case_q = []
for i in range(q):
    n = int(input())
    s = list(input())
    t = list(input())
    case_q.append((n, s, t))


for query in case_q:
    n, s, t = query
    i = n - 1
    while i >= 3:
        if s[i - 3 : i + 1] == ["T", "I", "O", "T"] and t[i - 3 : i + 1] == [
            "I",
            "S",
            "C",
            "T",
        ]:
            t[i - 3 : i + 1] = ["T", "I", "O", "T"]
        i -= 1
    if s == t:
        print("Yes")
    else:
        print("No")
