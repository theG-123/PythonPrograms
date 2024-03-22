#Write a program that reads the words in words.txt and stores them as keys in
#a dictionary. It doesn’t matter what the values are. Then you can use the in
#operator as a fast way to check whether a string is in the dictionary.

fhand = open('words.txt')
storedWords = dict()

for line in fhand:
    words = line.split()
    for word in words:
        storedWords [word] = storedWords.get(word,0) + 1
print (storedWords)