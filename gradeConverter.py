score = input ('Enter score: ')
try:
    fscore = float (score)
except:
    print ('Error, please enter a numerical input')
    quit ()
    
if fscore > 1.0 or fscore < 0.0:
    print ('Error: Credentials out of range. Enter a number between 0.0-1.0')
    quit ()
elif fscore >= 0.9:
    grade = "A"
elif fscore >= 0.8:
    grade = "B"
elif fscore >= 0.7:
    grade = "C"
elif fscore >= 0.6:
    grade = "D"
elif fscore < 0.6:
    grade = "F"
print (grade)

