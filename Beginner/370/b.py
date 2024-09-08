n = int(input())

atoms = []
for i in range(n):
    atoms.append(list(map(int, input().split())))


for i in range(n):
    if i == 0:
        current_atom = atoms[0][0]
    else:
        if current_atom - 1 >= i:
            current_atom = atoms[current_atom - 1][i]
        else:
            current_atom = atoms[i][current_atom - 1]

print(current_atom)
