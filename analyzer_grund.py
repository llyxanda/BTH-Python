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

