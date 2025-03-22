from itertools import combinations

a_7 = list(map(int, input().split()))

a_5 = list(combinations(a_7, 5))

for hand in a_5:
    hand_kinds = list(set(hand))
    if len(hand_kinds) != 2:
        continue
    for num in hand_kinds:
        if hand.count(num) in [2, 3]:
            print("Yes")
            exit()

print("No")
