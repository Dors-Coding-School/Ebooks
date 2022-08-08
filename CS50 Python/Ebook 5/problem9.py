def get_sum_digits(x):
  sum = 0
  isAlternateDigit = False
  while(x != 0):
    if isAlternateDigit:
      sum += x % 10
    isAlternateDigit = not isAlternateDigit
