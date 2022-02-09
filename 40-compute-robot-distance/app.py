import math

x, y = 0, 0

while True:
    str_input = input("Write a string like 'UP 5 / DOWN 3 / LEFT 3 / RIGHT 2' (in order, one by one): ")

    if str_input == "":
        break
    else:
        str_input = str_input.split()

        if str_input[0] == "UP":
            y = y + int(str_input[1])
        elif str_input[0] == "DOWN":
            y = y - int(str_input[1])
        elif str_input[0] == "LEFT":
            x = x - int(str_input[1])
        elif str_input[0] == "RIGHT":
            x = x + int(str_input[1])

print(int(round(math.sqrt(x**2 + y**2))))
