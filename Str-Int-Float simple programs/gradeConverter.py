print ('Convert your grade scores with this app!')

try:
    userScore = float (input ('Enter your grade: '))
except:
    print ('Bad score')
    quit ()

def getGrade (score):
    if userScore < 0.1 or userScore > 1.0:
        print ('Bad score')
        quit ()
    elif score >= 0.9:
       grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
       grade = 'C'
    elif score >= 0.6:
       grade = 'D'
    elif score  < 0.6:
       grade = 'F'
    return grade

print (getGrade(userScore))