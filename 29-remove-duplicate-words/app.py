strings = input("Write a white space separated strings: ")
strings = strings.split(" ")

new_list = []
for i in strings:
    i = i.strip().lower()

    if i not in new_list:
        new_list.append(i)

new_list.sort()
print(" ".join(new_list))
