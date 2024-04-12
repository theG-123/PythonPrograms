#Exercise 3: Write a program that reads a file and prints the letters in decreasing
#order of frequency.
#Your program should convert all the input to lower case and only count the letters
#a-z. Your program should not count spaces, digits, punctuation, or anything other
#than the letters a-z. Find text samples from several different languages and see
#how letter frequency varies between languages. Compare your results with the
#tables at https://wikipedia.org/wiki/Letter_frequencies

import time
import string

while True: #Opening the file
    chooseFile = input('What file do you wish to open? ')

    try: #If the file can be opened, we open it with a 'loading' animation
        openFile = open(chooseFile)
        print('\nOpening file', end='')
        dot_count = 0  #Counter variable to track the number of dots printed
        for _ in range(9):
            if dot_count == 3:  #Reset the counter and start printing dots again
                dot_count = 0
                print('\b\b\b   \b\b\b', end='', flush=True)  #Erase previous dots
                time.sleep(0.3)  # Pause for .3 seconds
            else:
                print('.', end='', flush=True)  # Print dots without newline and flush to show immediately
                dot_count += 1  # Increment the counter
                time.sleep(0.4)  # Pause for .3 seconds
        print('\n')
        break
    except:
        print('Error: File Could not be opened')
        continue

#Get the letters of the file and find how many times each letter is repeated
letterFrequency = dict()
for line in openFile:
    line = line.translate(str.maketrans('', '', string.punctuation)) #Getting rid of any type of punctuation
    line = line.rstrip()
    line = line.lower() # 
    words = line.split()
    for word in words:
        for letter in word:
            letterFrequency [letter] = letterFrequency.get(letter,0) + 1

print (sorted(letterFrequency.items()))