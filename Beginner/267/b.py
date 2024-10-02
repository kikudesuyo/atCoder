s = list(map(int, list(input())))

current_pins = {0: [7], 1: [4], 2: [2, 8], 3: [1, 5], 4: [3, 9], 5: [6], 6: [10]}
place_dict = {1: 3, 2: 2, 3: 4, 4: 1, 5: 3, 6: 5, 7: 0, 8: 2, 9: 4, 10: 6}

if s[0] == 1:
    print("No")
    exit()


for i in range(len(s)):
    if s[i] == 1:
        continue
    place = place_dict[i + 1]
    current_pins[place].remove(i + 1)


is_left_pins = []
for pins in current_pins.values():
    if len(pins) == 0:
        is_left_pins.append(False)
    else:
        is_left_pins.append(True)

step_count = 0
for is_left in is_left_pins:
    if is_left and step_count == 1:
        step_count = 0
    if is_left and step_count == 0:
        step_count += 1
    if step_count == 1 and not is_left:
        step_count += 1
    if step_count >= 2 and is_left:
        print("Yes")
        exit()
print("No")
