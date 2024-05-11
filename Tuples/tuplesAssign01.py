# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
# time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

storedTimes = dict()

while True:
    fGet = input ('What file would you wish to open? ')
    try:
        if fGet == '':
            fOpen = open ('mbox-short.txt')
        else:
            fOpen = open (fGet)
        break
    except:
        print ('Error: File could not be opened')
        continue

for line in fOpen:
    if line.startswith('From '):
        words = line.split()
        date = words [5]
        locateTime = date.find(':')
        time = date[:locateTime]
        storedTimes [time] = storedTimes.get(time,0) + 1

orderedTimes = []

for key,val in storedTimes.items():
    storedTimes =  sorted (storedTimes)
    newTup = (key,val)
    orderedTimes.append(newTup)

orderedTimes = sorted (orderedTimes)

for k,v in orderedTimes:
    print (k, v)