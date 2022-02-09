total = 0
while True:
    """ ejemplo de funcionamiento:
    1. Ejecutar programa
    2. Escribir 'D 300'
    3. Escribir 'D 300'
    4. Escribir 'W 200'
    5. Escribir 'D 100'
    6. Dejar vacio y pulsar enter
    7. Visualizar cálculo final """

    string = input("Write data!: ")
    if string == "":
        break
    else:
        string = string.split(" ")
        if string[0].upper() == "D":
            total = total + int(string[1])
        elif string[0].upper() == "W":
            total = total - int(string[1])

print(total)
