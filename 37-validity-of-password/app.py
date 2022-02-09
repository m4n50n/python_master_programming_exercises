import re
password=input("Enter a comma separated string: ")

items = list(password.split(","))

res = []
pass_seq= "^.*(?=.{6,12})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$]).*$"

for item in items:
    result = re.findall(pass_seq, item)
    if result:
        res.append(result)
if not res:
    print("Error")
else:
    print(res)
    