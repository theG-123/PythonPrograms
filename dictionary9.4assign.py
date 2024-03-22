fhand = open ('mbox-short.txt')
dictionary = {}
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        word = words [1]
        dictionary [word] = dictionary.get(word,0) + 1

maxValue = 0
mostRepeated = None

for key, value in dictionary.items():
    if value > maxValue:
        maxValue = value
        mostRepeated = key

print (mostRepeated, maxValue)