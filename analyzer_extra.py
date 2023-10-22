import analyzer_grund
import string
import time
import random

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


def random_text(duration):
    timing = float(duration)
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    weights = [5 if c in string.ascii_letters + ' ' else 4 if c in string.digits  else 1 for c in characters]
    start_time = time.time()
    end_time = start_time + timing
    total_report = {
        'words_tuples': [],
        'count_words': 0,
        'count_input_words': 0,
        'count_letters': 0,
        'time_elapsed': 0
        }

    while time.time() < end_time:
        sample_chars = random.choices(characters, k = 60, weights=weights)
        line = ''.join(sample_chars)
        report = analyzer_grund.create_report_per_line(line)
        for key in total_report:
            total_report[key] += report[key]

    report_wrong_words = analyzer_grund.get_wrong_entered_elements(total_report['words_tuples'])
    wrong_words_list = list(report_wrong_words['wrong_elements'].keys()) + \
                       list(report_wrong_words['extra_elements'].keys())
    words_to_compare = [word for word in total_report['words_tuples']
                        if (word[0] in wrong_words_list) or (word[1] in wrong_words_list)] 
    words_to_letters = analyzer_grund.tuples_for_letters(words_to_compare)
    report_wrong_letters = analyzer_grund.get_wrong_entered_elements(words_to_letters)

    letter_precision = round(report_wrong_letters['wrong_no']/total_report['count_letters'] * 100, 2)
    gross_wpm = total_report['count_input_words']/total_report['time_elapsed']*60
    return { 'letter_precision' : letter_precision,
             'gross_wpm': gross_wpm }

