n, t = int(input()), input()

directions = ["E", "S", "W", "N"]

axis = [0, 0]
current_direction_idx = 0
for i in range(n):
    if t[i] == "S":
        if directions[current_direction_idx] == "N":
            axis[1] += 1
        elif directions[current_direction_idx] == "W":
            axis[0] -= 1
        elif directions[current_direction_idx] == "S":
            axis[1] -= 1
        elif directions[current_direction_idx] == "E":
            axis[0] += 1
    else:
        current_direction_idx = (current_direction_idx + 1) % 4
print(axis[0], axis[1])
