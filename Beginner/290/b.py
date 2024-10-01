n, k = map(int, input().split())
s = input()
join_count = 0
answer = ""
for char in s:
    if char == "o":
        if join_count < k:
            join_count += 1
            answer += char
        else:
            answer += "x"
    else:
        answer += char
print(answer)
