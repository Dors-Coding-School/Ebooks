def last_digit(x,y):
 return abs(x % 10) == abs(y % 10)
# Prompt user for x
x = int(input("x: "))
y = int(input ("y: "))
# Call the function
print(last_digit(x,y))
