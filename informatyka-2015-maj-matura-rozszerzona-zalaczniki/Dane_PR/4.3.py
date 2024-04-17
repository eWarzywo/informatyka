with open('liczby.txt', 'r') as f:
    counter = 1
    for line in f:
        line.strip()
        if counter == 1:
            min = int(line,2)
            minPlace = counter
            max = int(line,2)
            maxPlace = counter
        liczba = int(line,2)
        if liczba > max:
            max = liczba
            maxPlace = counter
        if liczba < min:
            min = liczba
            minPlace = counter
        counter += 1 
        
    print("max = ", maxPlace, " min = ", minPlace)

        