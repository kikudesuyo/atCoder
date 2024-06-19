# n = int(input())

# cube_root = n ** (1 / 3)
# int_cube_root = int(cube_root) + 1
# max = 0
# count = 1
# for num in range(1, int_cube_root + 1):
#     if num**3 > n:
#         break
#     str_num = str(num**3)
#     reversed_str_num = str_num[::-1]
#     if str_num == reversed_str_num:
#         max = num**3
# print(max)


n = int(input())
max = 0
count = 1
while True:
    cube_num = count**3
    if cube_num > n:
        break
    str_cube_num = str(cube_num)
    reversed_cube_num = str(cube_num)[::-1]
    if str_cube_num == reversed_cube_num:
        max = cube_num
    count += 1

print(max)
