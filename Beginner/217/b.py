s_n = [input() for _ in range(3)]

contests = ["ABC", "ARC", "AGC", "AHC"]


for contest in contests:
    if contest not in s_n:
        print(contest)
        break
