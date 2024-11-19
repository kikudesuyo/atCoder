from collections import defaultdict

n = int(input())
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
box_map = defaultdict(set)
card_map = defaultdict(list)
for query in queries:
    if query[0] == 1:
        card_map[query[2]].append(query[1])
        box_map[query[1]].add(query[2])
    elif query[0] == 2:
        cards = card_map[query[1]]
        sorted_cards = sorted(cards)
        print(*sorted_cards)
    else:
        sorted_boxes = sorted(box_map[query[1]])
        print(*sorted_boxes)
