def test(x,y):
 sum = x + y
 if sum >= 10 and sum <= 20:
 return 30
 else:
 return sum
# Prompt user for y
x = int(input("x: "))
# Prompt user for y
y = int(input ("y: "))
# Call the function
print(test(x,y))
