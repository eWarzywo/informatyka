import random
price = round(random.uniform(1, 1000), 2)

print("The price is: " + str(price))

money = float(input("How much money do you have? "))
change = round(money - price, 2)

if change < 0:
    print("You don't have enough money!")
elif change == 0:
    print("You have the exact amount of money!")
else:
    bills = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]
    bills_counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # print(len(bills))
    # print(len(bills_counter))
    for i in range(len(bills)):
        while change >= bills[i]:
            if change // bills[i] >= 1:
                change -= bills[i]
                bills_counter[i] += 1
    # print(bills_counter)
    for i in range(len(bills)):
        if bills_counter[i] > 0:
            print("Give " + str(bills_counter[i]) + " x " + str(bills[i]))
