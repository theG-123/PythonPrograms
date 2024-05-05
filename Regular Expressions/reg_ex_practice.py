import re

def sum_numbers_in_file(file_name):
    total_sum = 0
    try:
        with open(file_name) as file_handle:
            for line in file_handle:
                line = line.rstrip()
                numbers = re.findall('[0-9]+', line)  # Regular expression to find integers
                for number in numbers:
                    total_sum += int(number)  # Convert and add each number to total_sum
        return total_sum
    except FileNotFoundError:
        print('File not found:', file_name)
        return None
    except Exception as e:
        print('Error occurred while processing the file:', e)
        return None

if __name__ == '__main__':
    file_to_open = input('What file would you like to open? ')
    while True:
        if file_to_open.strip():  # Check if the input is not empty
            result = sum_numbers_in_file(file_to_open)
            if result is not None:
                print('Sum of numbers in the file:', result)
            break
        else:
            print('Please enter a valid file name.')
            file_to_open = input('What file would you like to open? ')