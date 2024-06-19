n = int(input())

cube_root = n ** (1 / 3)
int_cube_root = int(cube_root) + 1
max = 0
count = 1
for num in range(1, int_cube_root + 1):
    if num**3 > n:
        break
    str_num = str(num**3)
    reversed_str_num = str_num[::-1]
    if str_num == reversed_str_num:
        max = num**3
print(max)
