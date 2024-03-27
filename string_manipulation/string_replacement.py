#Here we are using the built in command str.replace (new, old, [count]) In this code, the str is the variable called thePhrase
#The 'new' parameter means the things we are modifying/putting in this string and the old tells python what piece of the string
#should be removed and the new one will replace the old substring.

#!!THIS BUILT IN FUNCTION IS CASE SENSITIVE SO MAKE SURE TO TYPE THE OLD VALUES CORRECTLY BECAUSE IF NOT, IT WILL NOT DO IT!!

thePhrase = 'Hello world, Hello python, Hello world'
print ('String before .replace:', thePhrase)
modifiedPhrase = thePhrase.replace('Hello', 'hi', 2)
print ('String after  .replace:', modifiedPhrase)

#So here we are replacing the word 'Hello' in the string for 'hi': modifiedPhrase = thePhrase.replace('Hello', 'hi', 2)
#The number 2 at the end means how many times will that change will be made in case there are more Hello's in the string.
#You can just leave it blank and itll replace all the hello's but if you want to be specific in terms of how many times is the
#substring modified, you can use the count parameter after inputing the new,old in str.replace

#Now you will see what happens when I dont specify how many times will the change be made
randomPhrase = 'Hello Alex, Hello Christian, Hello Daniel'
print ('\nString before .replace:', randomPhrase) #checking the string before the .replace
changedPhrase = randomPhrase.replace('Hello', 'Hi')
print ('String after  .replace:', changedPhrase)

#because I didnt specify the number of times the process will be done
#it did it for all the Hello's and not only 1 or 2 if I had specified it to to so