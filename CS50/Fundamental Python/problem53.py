from cs50 import get_int
def get_sum_digits(x):
 sum = 0
 isAlternateDigit = False
 while(x != 0):
    if isAlternateDigit:
        sum += x % 10
    isAlternate = True
    x //= 10
 return sum
# Prompt user for x
x = get_int("x: ")
print(get_sum_digits(x))
