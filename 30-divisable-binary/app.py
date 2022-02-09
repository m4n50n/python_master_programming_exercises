digits = input("Write a comma separated 4 digit binary numbers: ")
digits = digits.split(",")

data = list(filter(lambda i: int(i, 2) % 5 == 0, digits))  # int(string,base)
print(",".join(data))
