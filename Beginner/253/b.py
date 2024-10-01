h, w = map(int, input().split())
s_n = [input() for _ in range(h)]


targets = []
for row in range(len(s_n)):
    for col in range(len(s_n[row])):
        if s_n[row][col] == "o":
            targets.append((row, col))


first_x, first_y = targets[0]
second_x, second_y = targets[1]
print(abs(first_x - second_x) + abs(first_y - second_y))
