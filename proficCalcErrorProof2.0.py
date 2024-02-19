

#Getting the hours worked and the rate of payment
hours = input ('Enter hours worked: ')
rate = input ('Enter payment rate: ')

#Converting the rate and hours numbers to decimals (float). If the input is a string print an error message and quit the program
try:
    fHours = float (hours)
    fRate = float (rate)
except:
    print ('Error, please enter a numeric input')
    quit ()

#calculate and print the gross pay
if fHours <= 40:
    pay = fHours * fRate
else:
    normalHours = 40
    overHours = fHours - 40
    pay = normalHours * fRate + overHours * fRate * 1.5
print (pay)
