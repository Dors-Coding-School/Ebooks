#Definition of function
def check_nums(x,y):
 if x == y:
 return (x+y)*3
 else:
 return x+y
# Prompt user for x
x = int(input("x: "))
# Prompt user for y
y = int(input ("y: "))
#Call the function
print(check_nums(x,y))
