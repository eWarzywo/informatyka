def letters(letter):
    letters = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'G': 16,
        'H': 17,
        'I': 18,
        'J': 19,
        'K': 20,
        'L': 21,
        'M': 22,
        'N': 23,
        'O': 24,
        'P': 25,
        'Q': 26,
        'R': 27,
        'S': 28,
        'T': 29,
        'U': 30,
        'V': 31,
        'W': 32,
        'X': 33,
        'Y': 34,
        'Z': 35 
    }
    return letters[letter]
with open("identyfikator_przyklad.txt", 'r') as file:
    wyniki = []
    wagi = [7,3,1,0,7,3,1,7,3]
    for line in file:
        line = line.strip()
        suma = 0
        for i in range(0,3):
            # print(line[i] , letters(line[i]) , wagi[i])
            suma += (letters(line[i]) * wagi[i])
        #     print(suma)
        # print("-----------------------------------------------")
        for i in range(4,len(wagi)):
            suma += (int(line[i]) * wagi[i])
        print(suma , line)
        if suma % 10 != int(line[3]):
            wyniki.append(line)
    print(wyniki)

