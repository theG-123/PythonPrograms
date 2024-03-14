dictionary = {}
fileOpen = open ('romeo.txt')
for line in fileOpen:
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word,0) + 1
print (dictionary)