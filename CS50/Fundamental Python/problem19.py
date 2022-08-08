from cs50 import get_int
def test(x,y):
 sum = x + y
 diff = abs(x - y)
 if sum ==5 or diff == 5 or x == 5 or y ==5:
    return True
 return False
# Prompt user for x
x = get_int("x: ")
# Prompt user for y
y = get_int("y: ")
print(test(x,y))
