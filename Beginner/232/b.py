s, t = input(), input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

s_idx, t_idx = alphabet.index(s[0]), alphabet.index(t[0])

diff = (t_idx - s_idx) % 26
for i in range(len(s)):
    if (alphabet.index(s[i]) + diff) % 26 != alphabet.index(t[i]):
        print("No")
        exit()
print("Yes")
