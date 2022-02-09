sentence = input("Write a sentence: ")

letters = 0
digits = 0
for e in sentence:
    if e.isnumeric():
        digits += 1
    elif e.isalpha():
        letters += 1

print(f"LETTERS {letters} DIGITS {digits}")
