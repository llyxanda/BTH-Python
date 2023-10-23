#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a file with functions for file analyzer
"""

from operator import itemgetter
import time
import analyzer_extra


def get_differing_elements(fill_value, list1, list2):
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


def get_input_and_time():
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

def get_report_per_line(line):
    print(line)
    wrong_wrong_words_tup = []
    line_input, elapsed_time = get_input_and_time()
    line_words, word_count, letter_count = count_words_and_letters(line)
    input_words = line_input.strip().split()
    if line_words != input_words:
        wrong_wrong_words_tup = get_differing_elements('', line_words, input_words)

    return {
        'wrong_words_tup': wrong_wrong_words_tup,
        'count_words': word_count,
        'count_input_words': len(input_words),
        'count_letters': letter_count,
        'time_elapsed': elapsed_time
    }

def get_report_per_file(file):
    """
    Function to print the content in a file, show the text row by row
    to the user and catch the words that are entered incorrectly by the user.
    Here we also return the total number of words and letters in the file as well as 
    timing the total input.
    """
    file_report = {
        'wrong_words_tup': [],
        'count_words': 0,
        'count_input_words': 0,
        'count_letters': 0,
        'time_elapsed': 0
        }
    with open(file, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            report = get_report_per_line(line)
            for key in report:
                file_report[key] += report[key]
    return file_report


def get_differing_letters(list_of_words):
    '''
    Function to go one level beyond words and create tupple for lettes in the text vs.
    letters inputed by the user. This is to be able to uae the calculate_wrong function but for letters
    instead of words
    '''
    letters_list  = []
    for tup in list_of_words:
        letters_list += get_differing_elements('',tup[0], tup[1])

    return letters_list

def get_wrong_entered_elements(list_of_elements):
    """
    Function to return the elemts (words or letters) entered wrong and how many times they occured
    """
    wrong_list = {}
    for element in list_of_elements:
             if element[0] != '': 
                if element[0] in wrong_list:
                     wrong_list[element[0]] += 1
                else:
                     wrong_list[element[0]] = 1
    sorted_wrong_list = dict(sorted(wrong_list.items(), key = lambda item: (item[1], item[0].islower()), reverse = True))
    
    return sorted_wrong_list

def get_final_report(file_name):
    '''
    Function to format the results as required in the specifications
    '''
    text_to_analize = get_report_per_file(file_name)
    minutes = int(text_to_analize['time_elapsed'] // 60)
    seconds = int(text_to_analize['time_elapsed'] % 60)

    total_words = text_to_analize['count_words']
    total_letters = text_to_analize['count_letters']

    count_wrong_words = len(text_to_analize['wrong_words_tup'])
    wrong_words_list =  text_to_analize['wrong_words_tup'] 

    words_to_letters = get_differing_letters(wrong_words_list)
    report_wrong_letters = get_wrong_entered_elements(words_to_letters)
    word_precision = round((1-count_wrong_words/total_words) * 100, 2)
    letter_precision = round((1-len(words_to_letters)/total_letters) * 100, 2)
    gross_wpm = text_to_analize['count_input_words']/text_to_analize['time_elapsed']*60
    net_wpm = gross_wpm - count_wrong_words/text_to_analize['time_elapsed']*60
    animal = analyzer_extra.assign_animal(net_wpm)
    
    return {'word_precision' : word_precision, 'letter_precision' : letter_precision,
            'report_wrong_letters': report_wrong_letters, 
             'gross_wpm': gross_wpm, 'net_wpm':net_wpm, 'animal':animal, 'minutes' : minutes,
             'seconds':seconds}

print(get_final_report("test.txt"))


def format_for_printing(final_report_dict):
    '''
    Function to format the results as required in the specifications
    '''
    string_to_print = '------------------------------Grunduppgifter---------------------------------\n'
    string_to_print += f"Ordprecision: {final_report_dict['word_precision']}%\n"
    string_to_print +=f"Teckenprecision:  {final_report_dict['letter_precision']}%\nFelstavade tecken:\n"
    for key, value in final_report_dict['report_wrong_letters'].items():
        string_to_print += f'{key}: {value}\n'
    string_to_print += f"Det tog {final_report_dict['minutes']} minuter och {final_report_dict['seconds']} sekunder\n"    
    string_to_print += '-----------------------------Extrauppgifter---------------------------------\n'
    string_to_print += f"Gross WPM: {round(final_report_dict['gross_wpm'], 1)}\n"
    string_to_print += f"Net WPM: {round(final_report_dict['net_wpm'], 1)}\n"
    string_to_print += f"Du skriver snabt som en {final_report_dict['animal']}.\n"
    return (string_to_print)


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

   