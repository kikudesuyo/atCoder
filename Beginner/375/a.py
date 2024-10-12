n = int(input())
s = input()

if n < 3:
    print(0)
    exit()
count = 0
for i in range(len(s) - 2):
    if s[i : i + 3] == "#.#":
        count += 1
print(count)
