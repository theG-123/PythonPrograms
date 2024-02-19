#There is a string method called count that is similar to the function
#in the previous exercise. Read the documentation of this method at:
# https://docs.python.org/library/stdtypes.html#string-methods
#Write an invocation that counts the number of times the letter a occurs in “banana”

#variable used for both examples
fruit = 'banana'

#the tryhard way to find how many times does a letter appear in a string
#this is also a dumb way of doing it because although its harder to do and flashy
#this can be made with just 2 lines of code using a built in command and achieve the same thing
#with the built in command there is little to no room for error in the code while this way can be tricky
#because one little thing that changes will damage the code completeley
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print ('The letter "a" is', count, 'times in banana')

#the smart way to find how many times does a letter appear in a string
#Here we use only 2 lines of code using the built in string.count() function in python
fruitCount = fruit.count('a')
print ('The letter "a" is', fruitCount, 'times in banana')

#In conclusion, by using built in functions in python, you can write code faster, simplify it and make debugging easier.