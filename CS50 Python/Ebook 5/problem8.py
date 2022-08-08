def get_sum_digits(x):
  sum = 0
  while(x != 0):
    sum += x % 10
    x //= 10
  return sum
