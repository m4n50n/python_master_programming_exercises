input_string = input("Enter a comma separated info: ")

info_list = [item.split(",") for item in input_string.split(" ")] 
print(sorted(info_list))
