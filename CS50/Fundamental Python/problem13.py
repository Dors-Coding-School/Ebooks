from cs50 import get_int

#Definition of function
def check_nums(x,y):
 if (x >= 100 and x <= 200) or (y >= 100 and y <= 200):
    return True
 return False

# Prompt user for x
x = get_int("x: ")
# Prompt user for y
y = get_int("y: ")
#Call the function
print(check_nums(x,y))
