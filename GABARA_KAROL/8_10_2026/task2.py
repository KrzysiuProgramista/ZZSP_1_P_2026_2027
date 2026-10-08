sentence = input("Enter a sentence: ")

print("Number of characters:",
      len(sentence))
print("Upper case:",
      sentence.upper())

words = sentence.split()
print("Number of words:",
      len(words))

print("Firstword:", words[0])
print("Lastword:", words[1])

print("Underscores:",
      sentence.replace(" ","_"))