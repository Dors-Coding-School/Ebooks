# Prompt user for number of rows
num_rows = get_int("Number of rows: ")
k = 1
for row in range(1, num_rows):
 for col in range(1, row+1):
   print(k, end="")
   k += 1
 print()
