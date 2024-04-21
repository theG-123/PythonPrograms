#Calculate the first 20 digits of the fibonacci sequence

while True:
    howManyNums = input('How many numbers from the fibbonaci sequence do you want to print out? ') 
    try:
        numbers = int (howManyNums)
        break
    except:
        print('Please enter a number')
        continue

fibonnacci_seq = [0,1]

for i in range (numbers):
    fibonnacci_seq.append(fibonnacci_seq[-1] + fibonnacci_seq[-2])

print (fibonnacci_seq)