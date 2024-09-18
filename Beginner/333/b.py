s_12 = input()
t_12 = input()

alphabet = "ABCDE"

s_1_index = alphabet.index(s_12[0])
s_2_index = alphabet.index(s_12[1])
t_1_index = alphabet.index(t_12[0])
t_2_index = alphabet.index(t_12[1])

s_length_type = abs(s_2_index - s_1_index)
t_length_type = abs(t_2_index - t_1_index)

if s_length_type == 3:
    s_length_type = 2
if t_length_type == 3:
    t_length_type = 2
if s_length_type == 4:
    s_length_type = 1
if t_length_type == 4:
    t_length_type = 1


if s_length_type == t_length_type:
    print("Yes")
else:
    print("No")
