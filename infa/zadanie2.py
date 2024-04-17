def podzialNaCzynniki(liczba):
    tab = []
    i = 2
    while (liczba > 1):
        if (liczba % i == 0):
            tab.append(i)
            liczba /= i
        else:
            i += 1
    return tab
def podzialNaRozneCzynniki(liczba):
    tab = podzialNaCzynniki(liczba)
    tab2 = []
    for i in tab:
        if i not in tab2:
            tab2.append(i)
    return tab2

with open("przyklad.txt", 'r') as file:
    # print(podzialNaCzynniki(420))
    max = 0
    max2 = 0
    liczba_najwiecej = 0
    liczba_najrozniejsza = 0
    for line in file:
        line = line.strip()
        if len(podzialNaCzynniki(int(line))) > max:
            max = len(podzialNaCzynniki(int(line)))
            liczba_najwiecej = int(line)
        if len(podzialNaRozneCzynniki(int(line))) > max2:
            max2 = len(podzialNaRozneCzynniki(int(line)))
            liczba_najrozniejsza = int(line)

    print('Liczba', liczba_najwiecej, 'ma najwiecej czynnikow pierwszych', max)
    print('Liczba', liczba_najrozniejsza, 'ma najwiecej roznych czynnikow pierwszych', max2)
