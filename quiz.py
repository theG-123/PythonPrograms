#Promp: Write a program that simulates a basic quiz. Create a list of questions and their corresponding correct answers.
#Allow the user to answer each question, and then provide them with a score at the end. Use a function called take_quiz to encapsulate the quiz logic.

#Me (to remember): I want a program that asks the user for the type of question he wants and based on the output of the user, a set of questions are asked.

correct = 0
incorrect = 0

print ('Test your knowledge with different types of questions to see how much you know!')

while True:
    question_type = input ('Select your question type: \n1: math \n2: general knowledge\n3: exit \nSelect: ')

#check if the question type is a valid type and if not print error message and start again
    if question_type.lower() not in ['1', '2', '3']:
        print ('Error: please select a valid question type prompted in the message or enter the "done" message to stop the quiz \n')
        continue
    if question_type.lower() == '3':
        print ('Quiz finished!')
        print ('Score: \n', correct, 'correct \n', incorrect, 'incorrect')
        quit ()
#math question/s
    if question_type.lower() == '1':
        question = input ("What is 2+2? ")
        try:
            answer = int(question)
        except:
            print ('Error: please enter a numeric input for this question \n')
            continue
        if answer == 4:
            print ('Correct! 2+2 is indeed',answer,'\n')
            correct = correct + 1
            continue
        else:
            print ('Wrong answer \n')
            incorrect = incorrect + 1
            continue
#general knowledge question/s
    if question_type.lower() == "2":
        question = input ('In what year did Christopher Colombus discover America? ')
        try:
            answer = int(question)
        except:
            print ('Error: please enter a valid year for this question \n')
            continue
    if answer == 1492:
        print ('Correct, America was discovered in', answer, '\n')
        correct = correct + 1
        continue
    else:
        print ('Wrong answer \n')
        incorrect = incorrect + 1
        continue