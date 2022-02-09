def digits_sum(num):
  total = 0

  for i in str(num):
    total += int(i)
  
  return total

print(digits_sum(123))