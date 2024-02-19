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