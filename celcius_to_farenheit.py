while True:
    getCelsius = input ('Enter temperature in celsius: ')

    try:
        celsius = float (getCelsius)
    except:
        print ('Enter a number')
        continue

    faren = (celsius * 9/5) + 32
    print (celsius, 'degrees celsius is', faren, 'degrees farenheit \n')
    
    closeProgram = input ('Do you want to keep running the program? Yes = y No = n \n')
    if closeProgram == 'n':
        break
    else:
        continue