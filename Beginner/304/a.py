n = int(input())

names, ages = [], []
for _ in range(n):
    name, age = input().split()
    names.append(name)
    ages.append(int(age))


min_age = min(ages)
idx = ages.index(min_age)

answer_names = names[idx:] + names[:idx]
for name in answer_names:
    print(name)
