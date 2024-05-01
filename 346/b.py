w, b = list(map(int, input().split()))

total_keys = w + b

s_elem = "wbwbwwbwbwbw"

max_loop_num = (int(total_keys / len(s_elem))) + 2

s = ""
for i in range(max_loop_num):
    s += s_elem

partial_str = ""
for j in range(len(s)):
    if len(partial_str) < total_keys:
        pass
    else:
        w_s = partial_str.count("w")
        b_s = partial_str.count("b")
        if w_s == w and b_s == b:
            print("Yes")
            exit()
        else:
            partial_str = partial_str[1:]
    partial_str += s[j]
print("No")
