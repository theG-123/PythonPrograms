#Write a program which repeatedly reads integers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average of the
#integers. If the user enters anything other than a integers, detect their mistake
#using try and except and print an error message and skip to the next integers

count = 0
total = 0
average = 0

while True:
    prompt = input ('Enter a number: ')
    if prompt.lower() == "done":
        break
    try:
        fPrompt = float (prompt)
        total = total + fPrompt
        count = count + 1
        average = total / count
    except:
        print ('Invalid input')
print (total, count, average)
