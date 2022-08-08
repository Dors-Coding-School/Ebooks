from cs50 import get_int
def test(x,y):
 sum = x + y
 if sum >= 10 and sum <= 20:
    return 30
 else:
    return sum
# Prompt user for x
x = get_int("x: ")
# Prompt user for y
y = get_int("y: ")
print(test(x,y))
