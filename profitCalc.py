#These were the insrurctions that the assignment had:
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5
#times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program(the pay should be 498.75).
#You should use input to read a string and float()to convert the string to a number. Do not worry about error checking the user input - assume the user types
#numbers properly.

#Comments that explain my code down:

#Getting the hours worked and the rate of payment
hours = input ('Enter hours worked: ')
rate = input ('Enter payment rate: ')

#Converting the rate and hours numbers to decimals (float)
iHours = float (hours)
iRate = float (rate)

#Check if the hours is less or more than 40 and from the hour 41 and on
#the pay rate will be multiplied by 1.5
if iHours <= 40:
    pay = iHours * iRate
else:
    normalHours = 40
    overHours = iHours - 40
    pay = normalHours * iRate + overHours * iRate * 1.5
print (pay)
