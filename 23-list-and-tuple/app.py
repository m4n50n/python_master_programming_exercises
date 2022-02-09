items = input("Insert numbers: ")
items = items.split(",")

new_list = []
for i in items:
    new_list.append(i.strip())

print(new_list)
