sentence = input("Enter a sentence: ")
print("Number of characters:", len(sentence))
print("Upper case:", sentence.upper())
words = sentence.split()
print("Number of words:", len(words))
if words:
    print(f"First word: {words[0]}, Last word: {words[-1]}")
else:
    print("No words entered.")
print("With underscores:", sentence.replace(" ", "_"))
