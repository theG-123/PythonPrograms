#Write another program that prompts for a list of numbers as above
#and at the end prints out both the maximum and minimum of the numbers instead
#of the average

max = None
min = None

while True:
    askNum = input ('Enter a number: ')
    if askNum.lower() == 'done':
        break
    try:
        fNum = float (askNum)
        if max == None or max < fNum:
            max = fNum
        if min == None or min > fNum:
            min = fNum
    except:
        print ('Invalid Input')
print ('Max is', max, 'and min is', min)