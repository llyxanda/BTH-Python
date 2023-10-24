
import time
from operator import itemgetter
import core_functions as cf


def random_test(duration):
    '''
    Function to show a random charachter, get an input from the user
    and calculate the imprecision, characters per min and list the wrong enetered characters
    '''
    print(f"Typing test: You have {duration} seconds.")

    start_time = time.time()
    input_char_count = count_char = 0
    error_count = {}
    
    while time.time()  < duration + start_time:
        remaining_time = int(start_time + duration - time.time())
        random_char = cf.generate_random_character()
        print(f"There are {remaining_time} seconds left!\nCharacter to type: \n {random_char}")
        count_char += 1
        user_input = input()
        input_char_count += 1
        if user_input != random_char:
            if random_char in error_count:
                error_count[random_char] += 1
            else:
                error_count[random_char] = 1

    char_per_min = (input_char_count / duration) * 60
    error_percentage = sum(value for value in error_count.values())/input_char_count

    sorted_errors = dict(sorted(error_count.items(), key = itemgetter(1), reverse=True))
    return char_per_min, error_percentage, sorted_errors
