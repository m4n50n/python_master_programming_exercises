digit = input("Insert a digit: ")

sum = 0
for i in range(1, 5):
    print(i)
    sum += int(digit * i)

print(sum)
