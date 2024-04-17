import random

n = int(input("Ile chcesz wygenerować haseł?"))
m = random.randint(5,20)
male_litery = "abcdefghijklmnopqrstuvwxyz"
duze_litery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cyfry = "0123456789"
specjalne = "!@#$%^&*()_+-="
czyDuze = input("Czy hasło ma zawierać duże litery? (t/n)")
czyCyfry = input("Czy hasło ma zawierać cyfry? (t/n)")
czySpecjalne = input("Czy hasło ma zawierać znaki specjalne? (t/n)")

with open("hasla.txt",'w') as f:
    for i in range(n):
        haslo = ""
        for j in range(m):
            if czyDuze == "n" and czyCyfry == "n" and czySpecjalne == "n":
                haslo += male_litery[random.randint(0,25)]
            elif czyDuze == "t" and czyCyfry == "n" and czySpecjalne == "n":
                if j == 0:
                    haslo += duze_litery[random.randint(0,25)]
                else:
                    haslo += male_litery[random.randint(0,25)]
            elif czyDuze == "n" and czyCyfry == "t" and czySpecjalne == "n":
                if j == 0:
                    haslo += cyfry[random.randint(0,9)]
                else:
                    haslo += cyfry[random.randint(0,9)]
            elif czyDuze == "n" and czyCyfry == "n" and czySpecjalne == "t":
                if j == 0:
                    haslo += specjalne[random.randint(0,11)]
                else:
                    haslo += specjalne[random.randint(0,11)]
            elif czyDuze == "t" and czyCyfry == "t" and czySpecjalne == "n":
                if j == 0:
                    haslo += cyfry[random.randint(0,9)]
                elif m == 1:
                    haslo += duze_litery[random.randint(0,25)]
                else: 
                    haslo += male_litery[random.randint(0,25)]
            elif czyDuze == "t" and czyCyfry == "n" and czySpecjalne == "t":
                if j == 0:
                    haslo += specjalne[random.randint(0,11)]
                elif j == 1:
                    haslo += duze_litery[random.randint(0,25)]
                else:
                    haslo += male_litery[random.randint(0,25)]
            elif czyDuze == "n" and czyCyfry == "t" and czySpecjalne == "t":
                if j == 0:
                    haslo += specjalne[random.randint(0,11)]
                elif j == 1:
                    haslo += cyfry[random.randint(0,9)]
                else:
                    haslo += male_litery[random.randint(0,25)]
            elif czyDuze == "t" and czyCyfry == "t" and czySpecjalne == "t":
                if j == 0:
                    haslo += specjalne[random.randint(0,11)]
                elif j == 1:
                    haslo += cyfry[random.randint(0,9)]
                elif j == 2:
                    haslo += duze_litery[random.randint(0,25)]
                else:
                    haslo += male_litery[random.randint(0,25)]
        f.write(haslo + "\n")