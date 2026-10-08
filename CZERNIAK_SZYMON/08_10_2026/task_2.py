sentence = input('Write the sentence:')

print(len(sentence.replace(' ', '')))
print(sentence.upper())

words = sentence.split()
print(len(words))

if words:
    print(words[0])
    print(words[-1])

print(sentence.replace(" ", "_"))
