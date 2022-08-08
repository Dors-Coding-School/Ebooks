num_rows = input("Number of rows: ")
for row in range(1, int(num_rows)):
    for col in range(1, row+1):
        print(row, end="")
    print()
