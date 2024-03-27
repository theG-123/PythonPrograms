#Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string, printing each letter on
#a separate line, except backwards

game = 'soccer'
reverseCount = len(game) - 1
while reverseCount >= 0:
    print (game [reverseCount])
    reverseCount = reverseCount - 1

print ('-----------------')

normalCount = 0
while normalCount < len(game):
    print (game[normalCount])
    normalCount = normalCount + 1