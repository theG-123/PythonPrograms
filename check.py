hrs = input ('Hours worked: ')
rt = input ('Rate per hour: ')

try:
    hours  = float (hrs)
    rate  = float (rt)
except:
    print ('Please enter a number')
    quit ()

if hours <= 40:
    pay = hours * rate
else:
    normHrs = 40
    overHrs = hours - normHrs
    pay = (normHrs * rate) + (rate * 1.5 * overHrs)

print (pay)
