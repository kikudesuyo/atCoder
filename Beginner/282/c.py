n = int(input())
s = list(input())

q_arr = []
count = 0
for i in range(n):
    if s[i] == '"':
        q_arr.append(i)

if len(q_arr) == 0:
    for i in range(n):
        if s[i] == ",":
            s[i] = "."
    print("".join(s))
    exit()

q_idx = 0
left_idx, right_idx = q_arr[q_idx], q_arr[q_idx + 1]
for i in range(n):
    if right_idx < i:
        if q_idx + 3 < len(q_arr):
            q_idx += 2
            left_idx, right_idx = q_arr[q_idx], q_arr[q_idx + 1]
    if left_idx < i < right_idx:
        pass
    else:
        if s[i] == ",":
            s[i] = "."

print("".join(s))
