n, m = map(int, input().split())
s_s = [input() for _ in range(n)]

result = m
for bit in range(1 << n):
    current_status = ["x"] * m
    str_boolean = bin(bit)[2:].zfill(n)
    for idx, boolean in enumerate(str_boolean):
        if boolean == "0":
            continue
        selected_shop = s_s[idx]
        for j in range(len(selected_shop)):
            if selected_shop[j] == "o":
                current_status[j] = "o"
        if current_status.count("o") == m:
            if result > str_boolean.count("1"):
                result = str_boolean.count("1")

print(result)
