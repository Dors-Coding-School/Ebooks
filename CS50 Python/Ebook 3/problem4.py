fruits = ["apple", "banana", "orange"]
while True:
 fruit = input("fruit: ")
 try:
   if fruit in fruits:
      print("We have this fruit!")
   break
 except:
   pass
