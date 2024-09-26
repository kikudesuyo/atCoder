n = int(input())

hex_num = hex(n)[2:].upper()
if len(hex_num) == 1:
    print("0" + hex_num)
else:
    print(hex_num)
