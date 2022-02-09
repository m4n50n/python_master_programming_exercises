all_even_digits_numbers = []
for i in range(1000, 3001):
    si = str(i)
    even_digits = True

    for char in si:
        char = int(char)
        if char % 2 != 0:
            even_digits = False

    if even_digits:
        all_even_digits_numbers.append(i)

print(all_even_digits_numbers)
