def get_sum_digits(x):
    sum = 0
    isAlternateDigit = False
    while(x != 0):
        if isAlternateDigit:
            sum += x % 10
        isAlternateDigit = not isAlternateDigit
        x //= 10
    return sum

# Prompt user for x
x = input("x: ")

print(get_sum_digits(int(x)))
