#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file
#in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

#Use the file name words.txt as the file name
chooseFile = input ('What file would you like to open? ')
try:
    fileOpen = open (chooseFile)
except:
    print ('Could not open file:', chooseFile)
    quit ()
for line in fileOpen:
    line = line.rstrip()
    print (line.upper())