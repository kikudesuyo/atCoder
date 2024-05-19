string = input()


partial_strings = []
for i in range(len(string)):
    for j in range(len(string) + 1):
        if not string[i:j] in partial_strings and string[i:j] != "":
            partial_strings.append(string[i:j])


print(len(partial_strings))
