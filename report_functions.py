#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a file with functions used for getting the actual results on a test
and reporting them - printing and writing scores in file.
These functions use core functions in the calculations.
"""

import core_functions as cf


def get_report_per_line(line):
    '''
    Function for getting the number of words, letters on a line, as well as the number of 
    words the user enters for that line, how long it takes for the user to type as well as
    returning tuples of the words that don't match or are extra or missing in the input vs the file.
    '''
    print(line)
    wrong_wrong_words_tup = []
    line_input, elapsed_time = cf.get_input_and_time()
    line_words, word_count, letter_count = cf.count_words_and_letters(line)
    input_words = line_input.strip().split()
    if line_words != input_words:
        wrong_wrong_words_tup = cf.get_differing_elements('', line_words, input_words)

    return {
        'wrong_words_tup': wrong_wrong_words_tup,
        'count_words': word_count,
        'count_input_words': len(input_words),
        'count_letters': letter_count,
        'time_elapsed': elapsed_time
    }

def get_report_per_test(file_name):
    """
    Function to sum up the calculations described above for all the lines in the file
    and thus get a report for the test.
    """
    file_report = {
        'wrong_words_tup': [],
        'count_words': 0,
        'count_input_words': 0,
        'count_letters': 0,
        'time_elapsed': 0
        }
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                report = get_report_per_line(line)
                for key, value in report.items():
                    file_report[key] += value
    except FileNotFoundError:
        print('This level file does not exist. Try another level!')
    return file_report


def get_test_results(file_name):
    '''
    Function to calculate the metrics needed for the result (precision, gross_wpm, net_wpm, etc.)
    using the test report from the previous function
    '''
    test_report= get_report_per_test(file_name)
    minutes = int(test_report['time_elapsed'] // 60)
    seconds = int(test_report['time_elapsed'] % 60)

    total_words = test_report['count_words']
    total_letters = test_report['count_letters']

    count_wrong_words = len(test_report['wrong_words_tup'])
    wrong_words_list =  test_report['wrong_words_tup'] 

    wrong_letters_list = cf.get_differing_letters(wrong_words_list)
    misspeled_letters = cf.get_wrong_entered_elements(wrong_letters_list)
    word_precision = round((1-count_wrong_words/total_words) * 100, 2)
    letter_precision = round((1-len(wrong_letters_list)/total_letters) * 100, 2)
    gross_wpm = test_report['count_input_words']/test_report['time_elapsed']*60
    net_wpm = gross_wpm - count_wrong_words/test_report['time_elapsed']*60
    animal = cf.assign_animal(net_wpm)
    
    return {'word_precision' : word_precision, 'letter_precision' : letter_precision,
            'misspeled_letters': misspeled_letters, 
             'gross_wpm': gross_wpm, 'net_wpm':net_wpm, 'animal':animal, 'minutes' : minutes,
             'seconds':seconds}


def format_for_printing(final_report_dict):
    '''
    Function to format the results as required in the specifications for printing
    '''
    string_to_print = '------------------------------Grunduppgifter---------------------------------\n'
    string_to_print += f"Ordprecision: {final_report_dict['word_precision']}%\n"
    string_to_print +=f"Teckenprecision:  {final_report_dict['letter_precision']}%\nFelstavade tecken:\n"
    for key, value in final_report_dict['misspeled_letters'].items():
        string_to_print += f'{key}: {value}\n'
    string_to_print += f"Det tog {final_report_dict['minutes']} minuter och {final_report_dict['seconds']} sekunder\n"    
    string_to_print += '-----------------------------Extrauppgifter---------------------------------\n'
    string_to_print += f"Gross WPM: {round(final_report_dict['gross_wpm'], 1)}\n"
    string_to_print += f"Net WPM: {round(final_report_dict['net_wpm'], 1)}\n"
    string_to_print += f"Du skriver snabt som en {final_report_dict['animal']}.\n"
    return (string_to_print)

def write_score_in_file(file, username, score, level):
    '''
    Function to write the result in the scores file
    '''
    try:
        with open(file, 'a', encoding='utf-8') as file_handle:
            file_handle.write(f"{username} {score} {level}\n")
    except (FileNotFoundError, PermissionError, IOError):
        print ('An error occured')

def show_sorted_results(file):
    '''
    Function to show the historic scores for menu choice 5. Sorted by level and score.
    '''
    results_dict = {}
    level_mapping = {'easy':1, 'medium':2, 'hard':3}
    try:
        with open(file, 'r', encoding='utf-8') as file_handle:
            for line in file_handle:
                result = line.strip().split()
                user, score, level = result[0], float(result[1]), result[2]
                results_dict[user] = (score, level, level_mapping[level]) 
        sorted_dict = dict(sorted(results_dict.items(), key = lambda item: (item[1][2], item[1][0]), reverse=True))
        print_string =''
        for result in sorted_dict.items():
            print_string += f"{result[0]}  {result[1][0]}  {result[1][1]}\n"
    except FileNotFoundError:
        print('No results found. Maybe you are the first user!')
    return print_string


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
