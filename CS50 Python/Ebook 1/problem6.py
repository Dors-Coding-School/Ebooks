def get_nearest(x,y):
 val = abs(x - 100)
 val2 = abs(y - 100)
 if val < val2:
 return x
 elif val > val2:
 return y
 else:
 return 0
# Prompt user for x, y
x = int(input("x: "))
y = int(input ("y: "))
print(get_nearest(x,y))
