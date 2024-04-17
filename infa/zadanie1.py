with open("przyklad.txt", "r") as file:
    counter = 0
    pierwsza = ""
    for line in file:
        line = line.strip()
        if line[0] == line[-1]:
            if pierwsza == "":
                pierwsza = line
            counter += 1
    print(counter, "a przykladem jest ", pierwsza)