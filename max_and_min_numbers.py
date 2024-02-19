#Prompt:
#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

max = None
min = None

while True:
    prompt = input ('Enter a number: ')
#check if the prompt is done, if it is then close the loop
    if prompt == 'done':
        break
#checking if the prompt is "floatable", if not, start again
    try:
        fprompt = float (prompt)
    except:
        print ('Invalid input')
        continue
#Check for the maximum number entered
    if max is None:
        max = fprompt
    elif max < fprompt:
        max = fprompt
#Check for the minimum number entered
    if min is None:
        min = fprompt
    elif min > fprompt:
        min = fprompt
maximum = int (max)
minumum = int (min)
#print the max and min numbers
print ('Maximum is', maximum,)
print ('Minimum is', minumum)