#This is a file opener with a user friendly menu that lets users choose a file
#and let users read, write, search for something... in the file selected

#Get the file name from the user
getFileName = input ('Select file: ')

#Check if the file is valid and send a message to the user (succesfull/unsuccesful) opening
try:
    fileOpen = open (getFileName)
    print ('File succesfully opened. What do you wish to do with the file? ')
except:
    print ('Error: File', getFileName, 'not found')
    quit ()

#Get input from the user to choose what does he want to do with the file. (read, write, search for something...)
fileReadingOptions = input ('1: Read file \n2: See the files length \n3: See how many characters does the file have \n4: Search for something specifically\nEnter number: ')

#reading the file
if fileReadingOptions == '1':
    for line in fileOpen:
        line  =  line.rstrip()
        print (line)
#Checking length of file (lines)
elif fileReadingOptions == '2':
    count = 0
    for line in fileOpen:
        line  =  line.rstrip()
        count =  count + 1
    print ('This file has a total of', count, 'lines!')
#Check how many characters the file has in total
elif fileReadingOptions == '3':
    totalCharacters = 0
    for line in fileOpen:
        totalCharacters = totalCharacters + len (line.rstrip())
    print ('The file', getFileName, 'has', totalCharacters, 'characters in total!')
#Searching for a specific thing on the file
elif fileReadingOptions == '4':
    fileSearch = input ('What do you want to search for?')
    for line in fileOpen:
        line = line.rstrip()
        if fileSearch in line:
            print(line)
else:
    print ('Invalid input: Please select a number between 1 and 4')