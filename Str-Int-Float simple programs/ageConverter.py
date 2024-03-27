#Create a function that takes the age in years and returns the age in days

while True:
    userInput = (input ('Find out your age in days! To exit the program type "done"\nHow old are you? '))
    if userInput == 'done':
        break
    else:
        getAge = int(userInput)
        def calcAge(age):
            calcDays = getAge * 365
            print (getAge, 'years is', calcDays, 'days\n')
        calcAge (getAge)