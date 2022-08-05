num_files = open('numbers.txt','w')
for i in range(1, 101):
 num_files.write(f"{str(i)}\n")
num_files.close()
