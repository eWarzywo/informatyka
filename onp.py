value = input("Enter a value: ")
print(value)
list = value.split()
print(list)
tempList = []
for i in range(len(list)):
    if list[i] == "+" or list[i] == "-" or list[i] == "*" or list[i] == "/":
        tempList.append(list[i])
    else:
        tempList.append(int(list[i]))
print(tempList)
stack = []
for i in range(len(tempList)):
    if tempList[i] == "+" or tempList[i] == "-" or tempList[i] == "*" or tempList[i] == "/":
        if tempList[i] == "+":
            stack.append(stack.pop() + stack.pop())
        elif tempList[i] == "-":
            stack.append(stack.pop() - stack.pop())
        elif tempList[i] == "*":
            stack.append(stack.pop() * stack.pop())
        elif tempList[i] == "/":
            stack.append(stack.pop() / stack.pop())
    else:
        stack.append(tempList[i])
print(stack)
print(stack.pop())
