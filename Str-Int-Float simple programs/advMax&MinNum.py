#This is the advanced way of finding the maximun and minimum numbers.

numList = []

while True:
    prompt = input ('Enter a number: ')
#check if the prompt is done, if it is then close the loop
    try:
        fprompt = float(prompt)
    except:
        if prompt.lower() == 'done':
            break
        else:
            print ('Invalid input')
            continue
    
    numList.append(fprompt)

    maxNumber = max(numList)
    minNumber = min(numList)
print (numList)
if numList == []:
    print('Error: No numbers entered')
else:
    print ('Maximum:', maxNumber, '\nMinumum:', minNumber)