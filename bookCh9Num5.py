#Exercise 5: This program records the domain name (instead of the address) where
#the message was sent from instead of who the mail came from (i.e., the whole email
#address). At the end of the program, print out the contents of your dictionary.

#So instead of getting the whole email like "bookCh9Num3.py", it only records the domain name for each email.

getFile = input ('Enter file name: ')
if getFile == '':
    fhand = open ('mbox-short.txt')
else:
    try:
        fhand = open (getFile)
    except:
        print ('File Not Found')
        exit ()

emailDomainName = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        word = words [1]
        getDomainName = word.find('@') + 1
        domain = word[getDomainName:]
        emailDomainName [domain] = emailDomainName.get(domain, 0) + 1
print (emailDomainName)