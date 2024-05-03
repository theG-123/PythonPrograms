import random
import string
import time

numbers = [str(i) for i in range(0, 10)]
alphabet_and_punctuation = list(string.ascii_letters + string.punctuation + ' ')
combined_list = alphabet_and_punctuation + numbers

def advancedPrint(chosen_phrase):
    phrase = ''
    index = 0
    progress = 0
    while phrase!= chosen_phrase:
        random_choice = random.choice(combined_list)
        phrase += random_choice
        print(phrase, end='\r')  # Print in place to show progress
        if phrase[index] == chosen_phrase[index]:
            index += 1
            progress += 1
        else:
            # Start again from the progress index
            phrase = chosen_phrase[:progress]
            index = progress
        time.sleep(0.05)  # Adjust the speed of printing for better visibility
    return phrase

advancedPrint('Hello, World!')
