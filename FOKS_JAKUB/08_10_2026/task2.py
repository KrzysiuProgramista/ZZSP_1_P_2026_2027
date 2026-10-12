sentence = input("please type your sentence: ")

words = sentence.split()

print('Number of characters:', len(sentence))
print("Uppercase:", sentence.upper())
print("Number of words:", len(words))
print("First word:", words[0])
print("Last word:", words[-1])
