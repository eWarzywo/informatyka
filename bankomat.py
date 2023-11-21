suma = 0 
with open("dane.txt", 'r') as file:
    content = file.read().split("\n")
    nominals = content[0].split(',')
    for i in range(len(nominals)):
        nominals[i] = int(nominals[i])
        
    quantity = content[1].split(',')
    for i in range(len(quantity)):
        quantity[i] = int(quantity[i])
        suma += nominals[i] * quantity[i]
        
banknow = len(nominals) - 1
akcja = input("Akcja: ")
kwota = int(input("Kwota: "))

if suma < kwota:
    print("Bankomat sie nie wyplaci")
    quit()

if akcja == 'w':
    while kwota > 0 and banknow >=0:
        if quantity[banknow]>0 and kwota >= nominals[banknow]:
            quantity[banknow] -= 1
            kwota -= nominals[banknow]
        else:
            banknow -= 1
with open('dane.txt', 'w') as file:

    for i in range(len(nominals)):
        nominals[i] = str(nominals[i])
    file.write(','.join(nominals) + '\n')

    for i in range(len(quantity)):
        quantity[i] = str(quantity[i])
    file.write(','.join(quantity))