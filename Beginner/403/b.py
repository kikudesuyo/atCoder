t = list(input())
u = list(input())


def is_subarray(sub, arr):
    n, m = len(arr), len(sub)
    for i in range(n - m + 1):
        if arr[i : i + m] == sub:
            return True
    return False


ques = []
for i in range(len(t)):
    if t[i] == "?":
        ques.append(i)
for i_1 in range(26):
    t[ques[0]] = chr(i_1 + 97)
    for i_2 in range(26):
        t[ques[1]] = chr(i_2 + 97)
        for i_3 in range(26):
            t[ques[2]] = chr(i_3 + 97)
            for i_4 in range(26):
                t[ques[3]] = chr(i_4 + 97)
                if is_subarray(u, t):
                    print("Yes")
                    exit()

print("No")
