with open("identyfikator.txt", "r") as file:
    wynik = []
    max = 0
    for linia in file:
        e = 0
        for i in range (3, 9):
            e += int(linia[i])
        if e > max:
            wynik = []
            max = e
            wynik.append(linia.replace("\n", ""))
        elif e == max: 
            wynik.append(linia.replace("\n", ""))
            max = e 
    print("\n--------------------\n")
    print(wynik)
