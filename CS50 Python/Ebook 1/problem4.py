#Definition of function
def check_nums(x,y):
 if x == 30 or y == 30 or x+y == 30:
 return True
 return False
# Prompt user for x
x = int(input("x: "))
# Prompt user for y
y = int(input ("y: "))
#Call the function
print(check_nums(x,y))
