s = input()

strings = []
for i in range(len(s)):
    shifted_str = s[i:] + s[:i]
    strings.append(shifted_str)


sorted_strings = sorted(strings)

print(sorted_strings[0])
print(sorted_strings[-1])
