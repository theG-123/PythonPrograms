numList = []
while True:
    prompt = input ('Enter a number: ')
#check if the prompt is done, if it is then close the loop
    try:
        int (prompt)
    except:
        if prompt == 'done':
            break
        else:
            print ('Invalid input')
            continue
    numList.append(prompt)
print (numList)
print ('Maximum:', max(numList), '\nMinumum:', min(numList))