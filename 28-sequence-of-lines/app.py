strings = input("Write a comma separated strings: ")
strings = strings.split(",")

new_list = []
for string in strings:
    new_list.append(string.strip().upper())

print(" ".join(new_list))
