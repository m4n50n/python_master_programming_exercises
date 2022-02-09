def getNumb(number):
    i = 0
    while i < number:
        n = i
        i = i + 1
        if n % 7 == 0:
            yield n

for i in getNumb(50):
    print(i)
