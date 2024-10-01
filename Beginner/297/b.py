s = input()

b_count = 0
r_count = 0
for i in range(len(s)):
    if s[i] == "B" and b_count == 0:
        x_idx = i
        b_count += 1
    if s[i] == "B" and b_count == 1:
        y_idx = i
    if s[i] == "R" and r_count == 0:
        r1_idx = i
        r_count += 1
    if s[i] == "R" and r_count == 1:
        r2_idx = i
    if s[i] == "K":
        k_idx = i


if (x_idx + y_idx) % 2 == 1:
    if r1_idx < k_idx < r2_idx:
        print("Yes")
    else:
        print("No")
else:
    print("No")
