
with open("liczby.txt", 'r') as f:
    counter = 0
    for line in f:
        line.strip()
        sumaZer = 0
        sumaJedynek = 0
        for i in range(len(line)):
            if line[i] == '0':
                sumaZer += 1
            if line[i] == '1':
                sumaJedynek += 1
        if sumaZer > sumaJedynek:
            counter += 1
    print("takich liczb jest", counter)