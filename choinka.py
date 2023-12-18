wielkosc = int(input("Podaj wielkosc choinki: "))

for i in range(wielkosc):
    print(" "*(wielkosc-i) + "*"*(i*2+1))
print(" "*(wielkosc) + "*")