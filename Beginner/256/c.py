from itertools import product, combinations

h1,h2,h3,w1,w2,w3 = map(int, input().split())


r1 = []
for elem in product(range(h1), repeat=3):
    if sum(elem) == h1-3:
        r1.append(list(map(lambda x: x+1, elem)))   

r2 = []
for elem in product(range(h2), repeat=3):
    if sum(elem) == h2-3:
        r2.append(list(map(lambda x: x+1, elem)))
    
r3 = []
for elem in product(range(h3), repeat=3):
    if sum(elem) == h3-3:
        r3.append(list(map(lambda x: x+1, elem)))
cnt = 0
for e1 in r1:
    for e2 in r2:
        for e3 in r3:
            if e1[0] + e2[0] + e3[0] == w1 and e1[1] + e2[1] + e3[1] == w2 and e1[2] + e2[2] + e3[2] == w3:
                cnt += 1
print(cnt)
