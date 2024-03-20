#Using dicctionaries to get the number of how many times a word or something specifically is repeated in a file

fileOpen = open ('romeo.txt')
dictionary = {}
repeatedNumber = 0

for line in fileOpen:
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word,0) + 1

for key, value in dictionary.items():
    if value > repeatedNumber:
        repeatedNumber = value
        mostRepeatedWord = key

print (mostRepeatedWord, repeatedNumber)