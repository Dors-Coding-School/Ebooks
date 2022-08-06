def test(x,y):
 sum = x + y
 diff = abs(x - y)
 if sum ==5 or diff == 5 or x == 5 or y ==5:
    return True
 return False
# Prompt user for y
x = int(input("x: "))
# Prompt user for y
y = int(input ("y: "))
print(test(x,y))
