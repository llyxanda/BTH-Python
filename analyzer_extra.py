import string
import time
import random
from operator import itemgetter

def assign_animal(net_wpm):
    if net_wpm < 10:
         animal = 'Sengångare'
    elif net_wpm < 20:
        animal = 'Snigel'
    elif net_wpm < 30:
        animal = 'Sjöko'
    elif net_wpm < 40:
        animal = 'Människa'
    elif net_wpm < 50:
        animal = 'Gasell'
    elif net_wpm < 60:
        animal = 'Struts'
    elif net_wpm < 70:
        animal = 'Gepard'
    elif net_wpm < 80:
        animal = 'Svärdfisk'
    elif net_wpm < 90:
        animal = 'Sporrgås'
    elif net_wpm < 100:
        animal = 'Taggstjärtseglare'
    elif net_wpm < 120:
        animal = 'Kungsörn'
    else:
        animal = 'Pilgrimsfalk'
    return animal


def generate_random_character():
    characters = string.ascii_letters + string.digits + string.punctuation
    return random.choice(characters)

def random_test(duration):
    print(f"Typing test: You have {duration} seconds.")

    start_time = time.time()
    input_char_count = count_char = 0
    error_count = {}
    
    while time.time()  < duration + start_time:
        random_char = generate_random_character()
        print(f"Character to type: {random_char}")
        count_char += 1
        user_input = input('Enter the charachter: ')
        input_char_count += 1
        if user_input != random_char:
            if random_char in error_count:
                error_count[random_char] += 1
            else:
                error_count[random_char] = 1

    char_per_min = (input_char_count / duration) * 60
    error_percentage = sum(value for value in error_count.values())

    sorted_errors = dict(sorted(error_count.items(), key = itemgetter(1), reverse=True))
    return char_per_min, error_percentage, sorted_errors
