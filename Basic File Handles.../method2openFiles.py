#this method will have the same output but it will be better because it's better to sort of skip the bad lines
#and then follow through for the good lines

openFile = open ('method2.txt')
for line in openFile:
    if not line.startswith('this'):
        continue
    line = line.rstrip()
#Using .rstrip() to eliminate the invisible /n for each line so they appear one below each other and not with a big space
#in between .strip() works also but you would also be removing possible indents or invisible spaces on the left
    print (line)