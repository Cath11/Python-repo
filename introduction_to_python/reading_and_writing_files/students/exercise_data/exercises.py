names = []

with open("names.txt") as txt_file:
    for line in txt_file:
        print(line)
        line = line.strip()
        names.append(line)
    for newline, value in enumerate("names.txt"): 
        

print(names)

with open("exercises.txt", "w+") as txt_file:
    for name in names:
        txt_file.write(name + '\n')