#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() 
#method. The program should build a list of words. For each word on each line check to see if the word is already in the
#list and if not append it to the list. When the program completes, sort and print the resulting words in python sort()
#order as shown in the desired output. You can download the sample data at http://www.py4e.com/code3/romeo.txt

#Getting input from the user
getFile = input ('What file would you like to open? ')

try:
    openFile = open(getFile)
except:
    print ('Error: Could not open file')
    exit ()

words_list = []

for line in openFile:
    # Split the line into words
    words = line.split()    
    # Iterate through each word in the line
    for word in words:
    # If the word is not already in the list, append it
        if word not in words_list:
            words_list.append(word)

# Sort the list of words
words_list.sort()

# Print the sorted list
print(words_list)