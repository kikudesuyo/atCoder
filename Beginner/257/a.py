n, x = map(int, input().split())

alphatbets = [chr(i).upper() for i in range(97, 97 + 26)]
strings = ""
for i in range(26):
    strings += alphatbets[i] * n

print(strings[x - 1])
