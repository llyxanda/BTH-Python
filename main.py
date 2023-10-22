#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the main program for the typing test application
"""
import analyzer_grund
import analyzer_extra


def main():
    '''
    Main function
    '''
    stop = False
    level_files = {'1': 'easy.txt', '2': 'medium.txt', '3': 'hard.txt'}
    level_mapping = {'1': 'easy', '2': 'medium', '3': 'hard'}
    SCORE_FILE = 'scores.txt'

    def menu_choice():
        '''
        Function for defining the menu choices
        '''
        print("1) Train easy")
        print("2) Train medium")
        print("3) Train hard")
        print("4) Show highest scores")
        print("5) Try a timed test with random characters")
        print("q) Quit.")
 

        choice = input("--> ")     
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            nonlocal stop
            stop = True

        elif choice in level_files:
            file_name = level_files[choice]
            level = level_mapping[choice]
            try:             
                result = analyzer_grund.get_final_report(file_name)
                input('Press [Enter] to see your results!')
                print(analyzer_grund.format_for_printing(result))
                input_username = input('Enter username to add to high scores: ')
                analyzer_grund.write_score_in_file(SCORE_FILE, input_username, result['word_precision'], level )
            except FileNotFoundError:
                print('Sorry this level is unavailable. Try another level!')

        elif choice == '4':
            try:
                print(analyzer_grund.show_sorted_results(SCORE_FILE))
            except FileNotFoundError:
                print('The score file seems to be missing!\n Maybe you are the first user')
        
        elif choice == '5':
            input_time = input('Enter the duration of the test in seconds: ')
            try:
                timing = float(input_time)
                test = analyzer_extra.random_test(timing)
                print(test)
            except TypeError:
                print('Please enter only numbers!')

    while not stop:
        menu_choice()


if __name__ == "__main__":
    main()    
