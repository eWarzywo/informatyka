def RecConversion(n):
    if n > 1: RecConversion(n // 2)
    print(n % 2 , end = "")
    return ""
print(RecConversion(12))