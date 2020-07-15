names = []

with open("names.txt") as txt_file:
    for line in txt_file:
        print(line)
        line = line.strip()
        names.append(line)

print(names)

with open("names_output.txt", "w") as txt_file:
    for name in names:
        txt_file.write(name + '\n')

