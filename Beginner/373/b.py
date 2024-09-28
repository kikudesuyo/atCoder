s = input()

dict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(s)):
    dict[s[i]] = i

count = 0
current_idx = dict["A"]
for i in range(len(alphabet)):
    current_alphabet = alphabet[i]
    count += abs(dict[current_alphabet] - current_idx)
    current_idx = dict[current_alphabet]
print(count)
