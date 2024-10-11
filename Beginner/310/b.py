n, m = map(int, input().split())

pcf = [list(map(int, input().split())) for _ in range(n)]


def is_fj_included_in_fi(fi, fj):
    flag = True
    for f2_elem in fj:
        if not f2_elem in fi:
            flag = False
            break
    return flag


# iが上位、jが下位かを確認
for i in range(n):
    pi, ci, fi = pcf[i][0], pcf[i][1], pcf[i][2:]
    for j in range(n):
        if i == j:
            continue
        pj, cj, fj = pcf[j][0], pcf[j][1], pcf[j][2:]
        if pi > pj:
            continue
        if ci < cj:
            continue
        if ci == cj and pi < pj and is_fj_included_in_fi(fi, fj):
            print("Yes")
            exit()
        if ci > cj and is_fj_included_in_fi(fi, fj):
            print("Yes")
            exit()
print("No")
