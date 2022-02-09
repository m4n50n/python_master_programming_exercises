def swap_digits(num):
  left = int(num / 10)
  right = num % 10
  
  return int(str(right) + str(left))

print(swap_digits(30))
