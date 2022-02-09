str_input = input("Write string like 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'")
str_input = str_input.split()

# https://www.programiz.com/python-programming/methods/built-in/set
# https://www.w3schools.com/python/ref_func_sorted.asp
items = set(str_input) # unordered list of unique str_input values
items = sorted(items) # ordered list

for item in items:
    print(f"{item}: {str_input.count(item)}")
