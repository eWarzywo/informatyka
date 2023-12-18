def isPalindrome(word) -> bool:
    if word  == word[::-1]: 
        return True
    else:
        return False 
with open("identyfikator.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if isPalindrome(line[0:3]) or isPalindrome(line[3:9]):
            print(line)