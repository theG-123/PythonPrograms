#HAZ MAS PROGRAMS DE LEER CONTENTS DE UN FILE CON SPECIFICATIONS TIPO CAPITALIZATION ETC.
#TIENES Q PRACTICAR MAS PA FAMILIARIZARTE CON EL TEMA BIEN

getFileName = input ('Select file: ') #Get the file name from the user

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
elif fileReadingOptions == '2':
#Checking length of file (lines)
    count = 0
    for line in fileOpen:
        line  =  line.rstrip()
        count =  count + 1
    print ('This file has a total of', count, 'lines!')
elif fileReadingOptions == '3':
#Check how many characters the file has in total
    length = 0 