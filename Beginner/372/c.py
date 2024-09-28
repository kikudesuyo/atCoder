n, q = map(int, input().split())
hoge = input()
s = []
for i in hoge:
    s.append(i)
xc_q = [list(input().split()) for _ in range(q)]


current_count = hoge.count("ABC")
answers = []
for x, c in xc_q:
    int_x = int(x)
    if s[int_x - 1] == c:
        answers.append(current_count)
        continue
    # 変える前
    if s[int_x - 1] == "A":
        if int_x <= len(s) - 2:
            if s[int_x] + s[int_x + 1] == "BC":
                if current_count != 0:
                    current_count -= 1
    elif s[int_x - 1] == "B":
        if 2 <= int_x <= len(s) - 1:
            if s[int_x - 2] + s[int_x] == "AC":
                if current_count != 0:
                    current_count -= 1
    elif s[int_x - 1] == "C":
        if 3 <= int_x <= len(s):
            if s[int_x - 3] + s[int_x - 2] == "AB":
                if current_count != 0:
                    current_count -= 1
    # 変える
    s[int_x - 1] = c
    if c == "A":
        if int_x <= len(s) - 2:
            if s[int_x] + s[int_x + 1] == "BC":
                current_count += 1
    elif c == "B":
        if 2 <= int_x <= len(s) - 1:
            if s[int_x - 2] + s[int_x] == "AC":
                current_count += 1
    elif c == "C":
        if 3 <= int_x <= len(s):
            if s[int_x - 3] + s[int_x - 2] == "AB":
                current_count += 1
    answers.append(current_count)


for i in answers:
    print(i)
