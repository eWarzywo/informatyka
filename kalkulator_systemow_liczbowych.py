# # z dziesietnego na binarny


# number = ""
# x = int(input())
# while(x>=1):
#     number += str(x%2)
#     x = x//2
# number = number[::-1]
# print(number)


# # z dziesietnego na wybrany


# number = "" 
# p = int(input("Podaj system: "))
# x = int(input())
# while(x>=1):
#     number += str(x%p)
#     x = x//p
# number = number[::-1]
# print(number)

# # z binarnego na dziesietny


# x = int(input())
# x = str(x)[::-1]
# number = 0
# for i in range(len(str(x))):
#     number += int(str(x)[i])*(2**i)
#     int(x)//10
# print(number)

# # z obojetnie jakiego systemu na dziesietny


# p = int(input("Podaj system: "))
# x = int(input())
# x = str(x)[::-1]
# number = 0
# for i in range(len(str(x))):
#     number += int(str(x)[i])*(p**i)
#     int(x)//10
# print(number)
