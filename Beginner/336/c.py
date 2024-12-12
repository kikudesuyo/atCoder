n = int(input())

cnt = n
if n <=5:
    print((n-1)*2)
    exit()
cnt -= 5

for digit in range(2, 100):
    if cnt >= 4*(5**(digit-1)):
        cnt -= 4*(5**(digit-1))
    else:
        break
if cnt == 0:
    print("8"*(digit-1))
    exit()


first_num = (cnt//(5**(digit-1))+1)*2
others_num = cnt%(5**(digit-1))-1

ans = list(str(first_num)+"0"*(digit-1))
idx = 1
while idx < digit:
    ans[idx] = str(others_num//(5**(digit-1-idx))*2)
    others_num = others_num%(5**(digit-1-idx))
    idx += 1

print("".join(ans))
