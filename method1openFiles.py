
readFile = open('method1.txt')
count = 0
for line in readFile:
    line = line.rstrip() 
#Using .rstrip() to eliminate the invisible /n for each line so they appear one below each other and not with a big space
#in between .strip() works also but you would also be removing possible indents or invisible spaces on the left
    print (line)
    count = count + 1
print ('Total lines: ', count)