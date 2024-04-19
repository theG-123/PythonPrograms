#Calculate the first 20 digits of the fibonacci sequence


fibonnacci_seq = [0,1]

for i in range (20):
    fibonnacci_seq.append(fibonnacci_seq[-1] + fibonnacci_seq[-2])

print (fibonnacci_seq)