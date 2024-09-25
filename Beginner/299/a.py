n = int(input())
s = input()

first_idx, target_idx, second_idx = 0, 0, 0
is_first_idx = False
for i in range(n):
    if not is_first_idx:
        if s[i] == "|":
            first_idx = i
            is_first_idx = True
    if is_first_idx:
        if s[i] == "|":
            second_idx = i
    if s[i] == "*":
        target_idx = i


if first_idx < target_idx < second_idx:
    print("in")
else:
    print("out")
