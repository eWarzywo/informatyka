with open('liczby.txt','r') as f:
    podzielnePrzez2 = 0
    podzielnePrzez8 = 0
    for line in f:
        line.strip()
        liczba = int(line,2)
        if liczba % 2 == 0:
            podzielnePrzez2 += 1
        if liczba % 8 == 0:
            podzielnePrzez8 += 1
    print("podzielnych przez 2 =",podzielnePrzez2, "podzielne przez 8 =",podzielnePrzez8)