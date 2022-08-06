#Definition of function
def check_nums(x,y):
 if (x >= 100 and x <= 200) or (y >= 100 and y <= 200):
 return True
 return False
# Prompt user for x, y
x = int(input("x: "))
y = int(input ("y: "))
#Call the function
print(check_nums(x,y))
