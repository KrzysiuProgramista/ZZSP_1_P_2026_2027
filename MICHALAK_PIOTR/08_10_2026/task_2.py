sent = input("Enter random sentence: ")
sentList = sent.split()

print(len(sent))
print(sent.capitalize())
print(sent.count(" ")+1)
print(sentList[0],sentList[len(sentList)-1])
print(sent.replace(" ", "_"))