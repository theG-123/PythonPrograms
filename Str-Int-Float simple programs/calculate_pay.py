# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for 
#the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to
# You can assume the user types numbers properly. Do not name your variable sum or use the sum() function

#Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters (hours and rate)

try:
    hrs = float (input ('Hours worked: '))
    rt = float (input ('Rate per hour: '))
except:
    print ('Error, please enter a numeric input')
    quit ()

def computepay (hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        normHrs = 40
        overHrs = hours - normHrs
        pay = (normHrs * rate) + (rate * 1.5 * overHrs)
    return pay

print ('Pay:', computepay (hrs, rt))