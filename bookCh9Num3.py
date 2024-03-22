#Exercise 3: Write a program to read through a mail log, build a histogram using
#a dictionary to count how many messages have come from each email address, and
#print the dictionary.

getFile = input ('Enter file name: ')
if getFile == '':
    fhand = open ('mbox-short.txt')
else:
    try:
        fhand = open (getFile)
    except:
        print ('File Not Found')
        exit ()

emailAdresses = dict()

for line in fhand:
    if line.startswith ('From '):
        words = line.split()
        email = words [1]
        emailAdresses [email] = emailAdresses.get(email,0) + 1
print (emailAdresses)
