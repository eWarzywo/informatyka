tab = [1,2,3,4,5,6,7]
x = int(input("Wprowadź szukany element "))
tab.append(x)
firstOccurence = 0
for i in range(len(tab)):
    if (tab[i] == x):
        firstOccurence = i
        break
if(firstOccurence == len(tab)-1):
    print("Znaleziono wartownika, nie ma takiej szukanej wartości w tablicy")
else:
    print("Pierwsze wystapienie szukanej to: ", firstOccurence)
tab.pop()
for i in range(len(tab)):
    print(tab[i], end=" ")

