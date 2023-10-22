#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a file with functions for file analyzer
"""

from operator import itemgetter
import time
import string
import random

def zip_2_lists(fill_value, list1, list2):
    '''
    Function to catch all the wrong entered words in the file text vs.
    user input and store it as tuples of form ([file word], [input word])
    '''
    zipped_list = []
    for idx in range(max(len(list1), len(list2))):
        try:
            if list1[idx] != list2[idx]:
                zipped_list.append((list1[idx], list2[idx]))
        except:
            if len(list1) > len(list2):
                zipped_list.append((list1[idx], fill_value))
            else:
                zipped_list.append((fill_value, list2[idx]))
    return zipped_list


def input_timing():
    '''
    Function to get the user input and time how long it taked for
    the user to input
    '''
    start_time = time.time()
    line_input = input('Your turn (press Enter when you are done): ')
    end_time = time.time()
    elapsed_time = end_time - start_time
    return line_input, elapsed_time


def count_words_and_letters(line):
    '''
    Function to count the number of words and letters for each row of the file
    and get a list of the words on the line.
    '''
    words = line.strip().split()
    word_count = len(words)
    letter_count = sum(len(word) for word in words)
    return words, word_count, letter_count

def create_report_per_line(line, wrong_words_tuples,no_words, no_letters , no_input_words, elapsed_time_total):
    print(line)
    line_input, elapsed_time = input_timing()
    elapsed_time_total += elapsed_time
    line_words, word_count, letter_count = count_words_and_letters(line)
    input_words = line_input.strip().split()
    if line_words != input_words:
        wrong_words_tuples += zip_2_lists('', line_words, input_words)
    no_words += word_count
    no_input_words += len(input_words)
    no_letters += letter_count

    return {
        'words_tuples': wrong_words_tuples,
        'count_words_file': no_words,
        'count_input_words': no_input_words,
        'count_letters_file': no_letters,
        'time_elapsed': elapsed_time_total
    }

def get_report_per_file(file):
    """
    Function to print the content in a file, show the text row by row
    to the user and catch the words that are entered incorrectly by the user.
    Here we also return the total number of words and letters in the file as well as 
    timing the total input.
    """
    wrong_words_tuples = []
    no_words = no_letters = no_input_words = elapsed_time_total = 0
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            report = create_report(line, wrong_words_tuples,no_words, no_letters , no_input_words, elapsed_time_total)
#            line_input, elapsed_time = input_timing()
#            elapsed_time_total += elapsed_time
#            line_words, word_count, letter_count = count_words_and_letters(line)
#            input_words = line_input.strip().split()
#            if line_words != input_words:
#                wrong_words_tuples += zip_2_lists('', line_words, input_words)
#            no_words += word_count
#            no_input_words += len(input_words)
#            no_letters += letter_count

    return report

def tuples_for_letters(list_of_words):
    '''
    Function to go one level beyond words and create tupple for lettes in the text vs.
    letters inputed by the user. This is to be able to uae the calculate_wrong function but for letters
    instead of words
    '''
    new_list = []
    for tup in list_of_words:
        new_list += zip_2_lists('',tup[0], tup[1])
    return new_list

def get_wrong_entered_elements(list_of_elements):
    """
    Function to return the elemts (words or letters) entered wrong and how many times they occured
    """
    wrong_list = {}
    extra_list = {}
    for element in list_of_elements:
             if element[0] != '': 
                if element[0] in wrong_list:
                     wrong_list[element[0]] += 1
                else:
                     wrong_list[element[0]] = 1
             else: 
                if element[1] in extra_list:
                     extra_list[element[1]] += 1
                else:
                     extra_list[element[1]] = 1
    wrong = len(list_of_elements)
    sorted_wrong_list = dict(sorted(wrong_list.items(), key = itemgetter(1), reverse = True))
    extra_wrong_list = dict(sorted(extra_list.items(), key = itemgetter(1), reverse = True))
    return ({'wrong_elements': sorted_wrong_list, 'extra_elements': extra_wrong_list, 'wrong_no': wrong })

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
    
def format_for_printing(file_name):
    '''
    Function to format the results as required in the specifications
    '''
    text_to_analize = get_report_per_file(file_name)
    minutes = int(text_to_analize['time_elapsed'] // 60)
    seconds = int(text_to_analize['time_elapsed'] % 60)

    total_words = text_to_analize['count_words_file']
    total_letters = text_to_analize['count_letters_file']

    report_wrong_words = get_wrong_entered_elements(text_to_analize['words_tuples'])
    wrong_words_list = list(report_wrong_words['wrong_elements'].keys()) + \
                       list(report_wrong_words['extra_elements'].keys())
    words_to_compare = [word for word in text_to_analize['words_tuples'] 
                        if (word[0] in wrong_words_list) or (word[1] in wrong_words_list)] 
    words_to_letters = tuples_for_letters(words_to_compare)
    report_wrong_letters = get_wrong_entered_elements(words_to_letters)
    word_precision = round((1-report_wrong_words['wrong_no']/total_words) * 100, 2)
    letter_precision = round((1-report_wrong_letters['wrong_no']/total_letters) * 100, 2)
    gross_wpm = text_to_analize['count_input_words']/text_to_analize['time_elapsed']*60
    net_wpm = gross_wpm - report_wrong_words['wrong_no']/text_to_analize['time_elapsed']*60
    animal = assign_animal(net_wpm)

    string_to_print = '------------------------------Grunduppgifter---------------------------------\n'
    string_to_print += f'Ordprecision: {word_precision}%\n'
    string_to_print +=f'Teckenprecision:  {letter_precision}%\nFelstavade tecken:\n'
    for key, value in report_wrong_letters['wrong_elements'].items():
        string_to_print += f'{key}: {value}\n'
    string_to_print += f"Det tog {minutes} minuter och {seconds} sekunder\n"    
    string_to_print += '-----------------------------Extrauppgifter---------------------------------\n'
    string_to_print += f"Gross WPM: {round(gross_wpm, 1)}\n"
    string_to_print += f"Net WPM: {round(net_wpm, 1)}\n"
    string_to_print += f"Du skriver snabt som en {animal}.\n"
    return (string_to_print, word_precision)



def write_score_in_file(file, username, score, level):
    try:
        with open(file, 'a', encoding='utf-8') as file_handle:
            file_handle.write(f"{username} {score} {level}\n")
    except:
        print ('An error occured')


def show_sorted_results(file):
    results_dict = {}
    level_mapping = {'easy':1, 'medium':2, 'hard':3}
    with open(file, 'r', encoding='utf-8') as file_handle:
        for line in file_handle:
            result = line.strip().split()
            user, score, level = result[0], float(result[1]), result[2]
            results_dict[user] = (score, level, level_mapping[level]) 
    sorted_dict = dict(sorted(results_dict.items(), key = lambda item: (item[1][2], item[1][0]), reverse=True))
    print_string =''
    for result in sorted_dict.items():
        print_string += f"{result[0]}  {result[1][0]}  {result[1][1]}\n"
    return print_string



def random_text(duration):
    timing = float(duration)
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    weights = [5 if c in string.ascii_letters + ' ' else 4 if c in string.digits  else 1 for c in characters]

    print(timing)
    start_time = time.time()
    end_time = start_time + timing
    elapsed_time_total = 0
    wrong_words_tuples = []
    no_words = no_letters = no_input_words = elapsed_time_total = 0

    while time.time() < end_time:
        sample_chars = random.choices(characters, k=60, weights=weights)
        line = ''.join(sample_chars)
        report = create_report_per_line(line)


""" 
def write_sorted_in_file(username, score, level):
    try:
        with open('scores.txt', 'r', encoding='utf-8') as file_handle:
            line_number = 1 
            level_mapping = {'easy':1, 'medium':2, 'hard':3}
            level_new_result = level_mapping[level]
            contents = file_handle.readlines()
            for line in contents:
                words = line.strip().split()
                level_line = level_mapping[words[2]]
                if level in line:
                    if float(score) >= float(words[1]):
                            break
                else:
                    if level_line <= level_new_result:
                        break
                line_number += 1

        contents.insert(line_number - 1, f"{username} {score} {level}\n")

        with open("scores.txt", "w", encoding='utf-8') as file_handle:
            contents = "".join(contents)
            file_handle.writelines(contents)
    except FileNotFoundError:
        with open('scores.txt', 'w', encoding='utf-8') as file_handle:
            file_handle.write(f"{username} {score} {level}\n")
 """

   