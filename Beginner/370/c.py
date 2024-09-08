s = input()
t = input()

initial_index = []
next_index = []
for i in range(len(s)):
    if s[i] > t[i]:
        initial_index.append(i)
    else:
        next_index.append(i)


strings = []
for i in range(len(initial_index)):
    s = s[: initial_index[i]] + t[initial_index[i]] + s[initial_index[i] + 1 :]
    strings.append(s)
for i in range(len(next_index) - 1, -1, -1):
    s = s[: next_index[i]] + t[next_index[i]] + s[next_index[i] + 1 :]
    strings.append(s)


print(len(strings))
for i in strings:
    print(i)
