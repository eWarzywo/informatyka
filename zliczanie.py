#zliczanie ilosci wystapien slow w tekście

X = input("Podaj tekst: ")
Y = input("Podaj szukaną frazę: ")
counter = 0
for i in range(len(X)):
    check = True
    for j in range(len(Y)):
        if (i+j) < len(X):
            if X[i+j] != Y[j]:
                check = False       
        else:
            check = False
    if check:
        counter += 1

print(counter)
print("W tekście jest", X.count(Y), "wystąpień frazy", Y)