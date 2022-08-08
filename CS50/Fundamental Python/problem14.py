from cs50 import get_int

# Prompt user for x
x = get_int("x: ")
count_quarters = 0
while (x >= 25):
 x -= 25
 count_quarters += 1
print(count_quarters)
