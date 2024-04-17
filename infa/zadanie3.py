#nie da rady :(((((

def dobraTrojka(x,y,z):
    if x!=y and x!=z and y!=z:
        if x != 0 and z!= 0:
            if y%x==0 and z%y==0:
                return True
    return False
# def dobraPiatka(u,w,x,y,z):
#     x = 0
def znajdzDzielnikiWTablicy(liczba, rekordy):
    tab = []
    for i in range(0,len(rekordy)):
        if liczba%rekordy[i] == 0:
            tab.append(rekordy[i])
    return tab

with open("przyklad.txt", 'r') as file:
    counter_dobre_trojki = 0
    for line in file:
        line = line.strip()
        line = line[::-1]
    print(counter_dobre_trojki)

        