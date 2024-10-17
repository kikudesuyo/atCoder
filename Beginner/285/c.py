s = input()
reversed_s = s[::-1]
alphabets = {}
for idx in range(26):
    alphabets[chr(65 + idx)] = idx + 1

count = 0
for idx in range(len(s)):
    alphabet = reversed_s[idx]
    num = alphabets[alphabet]
    count += 26**idx * num
print(count)
