with open('pesele.txt','w') as f:
    ilosc = int(input('Ile peseli wygenerować: '))
    data = []
    print('Podaj rrrr/mm/dd: ')
    for i in range(3):
        data.append(input())
    data[0] = data[0][2:4]
    data.append(input('Podaj płeć ( M / K ) '))
    if data[3] == 'K':
        data[3] = 0
    else:
        data[3] = 1
    if int(data[0]) >= 1800 and int(data[0]) <= 1899:
        data[1] = str(int(data[1]) + 80)
    elif int(data[0]) >= 2000 and int(data[0]) <= 2099:
        data[1] = str(int(data[1]) + 20)
    elif int(data[0]) >= 2099 and int(data[0]) <= 2199:
        data[1] = str(int(data[1]) + 40)
    elif int(data[0]) >= 2200 and int(data[0]) <= 2299:
        data[1] = str(int(data[1]) + 60)
    elif int(data[0]) >=1900 and int(data[0]) <= 1999:
        if data[1] < 10:
            data[1] = "0" + str(data[1])
    PPP = 000
    if int(data[1]) < 10 and int(data[1]) > 0:
        data[1] = "0" + str(data[1])
    if int(data[2]) < 10 and int(data[2]) > 0:
        data[2] = "0" + str(data[2])
    
    for i in range(ilosc):
        if PPP < 10 and PPP >= 0:
            dodawanePPP = "00" + str(PPP)
        elif PPP >= 10 and PPP < 100:
            dodawanePPP = "0" + str(PPP)
        PPP += 1
        linia = str(data[0]) + str(data[1]) + str(data[2]) + str(dodawanePPP) + str(data[3])[-1]
        wagi = [1,3,7,9,1,3,7,9,1,3]
        suma = 0
        for j in range(len(linia)):
            suma += (int(linia[j])* wagi[j]) % 10
        if (suma > 9):
            suma = suma % 10
        suma = 10 - suma
        if (suma == 10):
            suma = 0
        linia += str(suma)
        print("Dane testowe ----> "+str(linia) + " " + str(len(linia)) + " ||  "+ str(data[0])+ " " + str(data[1]) + " " + str(data[2])+ " " +str(dodawanePPP) + " " + str(suma))
        f.write("%s\n" % linia)
        data[3] += 2


            