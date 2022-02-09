sentence = input("Write a sentence: ")
sentence = sentence.split(",")

numbers = []
for i in sentence:
    if int(i) % 2 != 0:
        numbers.append(i)

print(",".join(numbers))
