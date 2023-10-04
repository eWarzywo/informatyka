def optimised_euklides(a, b):
    while b!=0:
        pom = b
        b = a%b
        a = pom
    return a



print("1 - Dodawanie ")
print("2 - Odejmowanie ")
print("3 - Mnożenie ")
print("4 - Dzielenie ")
choose  = int(input("Wybierz dzialanie "))
l1 = int(input("podaj l1: "))
m1 = int(input("podaj m1: "))
l2 = int(input("podaj l2: "))
m2 = int(input("podaj m2: "))
if choose == 1:
    pom = optimised_euklides(m1,m2)*m2
    l1 = l1*(pom/m1)
    l2 = l2*(pom/m2)
    # print("[",l1+l2,"/",pom,"]") dzialanie przed nwd
    print("skrocony ulamek: [",(l1+l2)//optimised_euklides(l1+l2,pom),"/",pom//optimised_euklides(l1+l2,pom),"]")

if choose == 2:
    pom = optimised_euklides(m1,m2)*m2
    l1 = l1*(pom/m1)
    l2 = l2*(pom/m2)
    # print("[",l1-l2,"/",pom,"]") dzialanie przed nwd
    print("skrocony ulamek: [",(l1-l2)//optimised_euklides(l1-l2,pom),"/",pom//optimised_euklides(l1-l2,pom),"]")

if choose == 3:
    # print("[",l1*l2,"/",m1*m2,"]") dzialanie przed nwd
    print("skrocony ulamek: [",(l1*l2)//optimised_euklides(l1*l2,m1*m2),"/",(m1*m2)//optimised_euklides(l1*l2,m1*m2),"]")
if choose == 4:
    # print("[",l1*m2,"/",m1*l2,"]") dzialanie przed nwd
    print("skrocony ulamek: [",(l1*m2)//optimised_euklides(l1*m2,m1*l2),"/",(m1*l2)//optimised_euklides(l1*m2,m1*l2),"]")