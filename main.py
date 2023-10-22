#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the main program for the typing test application
"""
import analyzer


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
        print("q) Quit.")
 

        choice = input("--> ")     
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            nonlocal stop
            stop = True

        elif choice in level_files:
            file_name = level_files[choice]
            level = level_mapping[choice]             
            result = analyzer.format_for_printing(file_name)
            print(result)
            input_username = input('Enter username to add to high scores: ')
            analyzer.write_score_in_file(SCORE_FILE, input_username, result[1], level )
        
        elif choice == '4':
            print(analyzer.show_sorted_results(SCORE_FILE))
        
        elif choice == '5':
            input_time = input('Enter the duration of the test in seconds: ')
            #try:
            timing = float(input_time)
            test = analyzer.random_text(timing)
            print(test)
           # except TypeError:
            #    print('Please enter only numbers!')

    while not stop:
        menu_choice()


if __name__ == "__main__":
    main()    
