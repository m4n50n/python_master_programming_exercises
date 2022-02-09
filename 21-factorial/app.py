def factorial(integer):
    total = 1
    for i in  range(1, integer + 1):
        total = total * i

    return total

print(factorial(8))
