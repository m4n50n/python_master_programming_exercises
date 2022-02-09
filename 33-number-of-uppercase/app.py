sentence = input("Write a sentence: ")

upper = 0
lower = 0
for e in sentence:
    if e.isupper():
        upper += 1
    elif e.islower():
        lower += 1

print(f"UPPER CASE {upper} LOWER CASE {lower}")
