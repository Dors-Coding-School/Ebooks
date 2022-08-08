from cs50 import get_int
def get_nearest(x,y):
 val = abs(x - 100)
 val2 = abs(y - 100)
 if val < val2:
    return x
 elif val > val2:
    return y
 else:
    return 0
# Prompt user for x
x = get_int("x: ")
# Prompt user for y
y = get_int("y: ")
print(get_nearest(x,y))
