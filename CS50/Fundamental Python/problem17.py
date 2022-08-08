from cs50 import get_int
def last_digit(x,y):
 return abs(x % 10) == abs(y % 10)
# Prompt user for x
x = get_int("x: ")
# Prompt user for y
y = get_int("y: ")
print(last_digit(x,y))
