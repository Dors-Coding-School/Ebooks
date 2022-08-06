while True:
 numbers = input("Numbers: ")
 try:
   number1, number2 = numbers.split(“,”)
   result = int(number1) + int(number1)
   print(result)
   break
 except:
   pass
