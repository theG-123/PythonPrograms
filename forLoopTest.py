#Examples of different uses of for loops

for i in range (5):
    print (i)
    if i>2:
        print ('Bigger than 2')
    print ('Done with i',i)
print ('ALL Done')
#Counting how many items are in a list
count = 0
people = ['Fred', 'Glenn', 'Dan', 'George']
for i in people:
    count = count + 1
    print ('Hello,', i)
print (count)

#finding the biggest and smallest numbers in a list
max = None
min = None
numbers = [10, 1, 7, 3.2, 22, 50, 40]

for i in numbers:
    if min is None or i < min:
        min = i

    if max is None or i > max:
        max = i

print ('The biggest number is', max)
print ('The smallest number is', min)

#finding what is the total of all the numbers added in a list
total = 0
numList = [10, 1, 7, 3.2, 22, 50, 40]
for i in numList:
    total  = total + i
print ('The total is', total)