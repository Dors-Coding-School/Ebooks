fruits = {"apple":1 , "banana": 3, "orange": 2}
while True:
 fruit = input("fruit: ")
 try:
  if fruit in fruits:
    print(fruits[fruit])
  break
 except:
  pass
