import math
def szyfrowanie(tekst,wybrane):
    X = []
    ilosc_tabel = len(wybrane)
    ilosc_wierszy = math.ceil(len(tekst)/ilosc_tabel)
    for i in range(ilosc_tabel):
        T = []
        for j in range(ilosc_wierszy):
            T.append('*')
        X.append(T)
    counter = 0
    for i in range(len(X)):
        for j in range(len(X[i])):
            if counter < len(tekst):
                X[i][j] = tekst[counter]
            counter+=1
    wynik = ""
    for i in range(len(X)):
        for j in range(len(X[i])):
            wynik += X[wybrane[i]-1][j]
    print(wynik)
    return wynik

def odszyfrowanie(tekst,wybrane):
    wynik = ""
    X = []
    counter = 0 
    for i in range (len(wybrane)):
        T = []
        for j in range(math.ceil(len(tekst)/len(wybrane))):
            T.append(tekst[counter])
            counter += 1
        X.append(T)
    T = []
    for i in range (len(wybrane)):
        T.append(X[wybrane[i]-1])
    for i in range (len(T)):
        for j in range (len(T[i])):
            wynik += T[i][j]
    wynik = wynik.replace('*','')
    print(wynik)
    return wynik

tekst = "tajny_tekst"
wybrane = [2,1,3,4,5]
odszyfrowanie(szyfrowanie(tekst,wybrane), wybrane)




