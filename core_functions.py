#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a file with core functions for the typing test.
Core functions are functions that are used in the calculation of the results
and that do not depend on other user defined functions.
"""

import time
import string
import random


def get_differing_elements(fill_value, list1, list2):
    '''
    Function to catch all the wrong entered words/letters in the file text vs.
    user input and store it as tuples of form ([file word], [input word])
    It retuns bot misspelings, and extra words/letters
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
    line_input = input('Your turn:: ')
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


def get_wrong_entered_elements(list_of_elements):
    """
    Function to return the elemts (words or letters) entered wrong,
    excluding the extra words that the user inputs (This is for the requirement
    to list the wrong entered letters and occurences - so exclusing the letters that were extered extra)
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

def get_differing_letters(list_of_words):
    '''
    Function to go one level beyond words and create tupple for wrong entered letters.
    '''
    letters_list  = []
    for tup in list_of_words:
        letters_list += get_differing_elements('',tup[0], tup[1])

    return letters_list


def generate_random_character():
    '''
    Function to generate a random characther for the test
    '''
    characters = string.ascii_letters + string.digits + string.punctuation
    return random.choice(characters)

def assign_animal(net_wpm):
    '''
    Function to assign an animal based on the user result net words per minute 
    '''
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