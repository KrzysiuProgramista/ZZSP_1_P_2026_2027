sent = str(input("Print me the a sentence: "))

print(len(sent))
print(sent.upper())
print(sent.count(" ")+1)
Sent = sent.split()
print(Sent[0],Sent[-1])
print(sent.replace(" ","_"))