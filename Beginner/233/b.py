l, r = map(int, input().split())
s = input()
left = s[: l - 1]
parital_str = s[l - 1 : r]
right = s[r:]
print(left + parital_str[::-1] + right)
