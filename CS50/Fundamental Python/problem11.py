from cs50 import get_int

#Definition of function
def check_nums(x,y):
 if x == y:
 return (x+y)*3
 else:
 return x+y

# Prompt user for x
x = get_int("x: ")
# Prompt user for y
y = get_int("y: ")
#Call the function
print(check_nums(x,y))
