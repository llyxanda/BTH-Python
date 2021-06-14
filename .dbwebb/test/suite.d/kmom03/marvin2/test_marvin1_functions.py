#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
from unittest import TextTestRunner
from examiner.exam_test_case import ExamTestCase
from examiner.exam_test_result import ExamTestResult
from examiner.helper_functions import import_module
from examiner.helper_functions import find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
main = import_module(REPO_PATH, 'main')
marvin = import_module(REPO_PATH, 'marvin')



class Test1Marvin1Functions(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)


    def check_print_contain(self, inp, correct, func):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                func()
                str_data = fake_out.getvalue()
                for val in correct:
                    self.assertIn(val, str_data)



    def test_main(self):
        """
        Testar att anropa menyvalen 1 och 7 via main funktionen i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["1", "7", "marvin1"]
        self.norepr = True
        self._multi_arguments = ["1", "dbwebb är bäst", "", "7", "sirapigt", "", "q"]
        self.check_print_contain(self._multi_arguments, ["dbwebb är bäst", "No match!"], main.main)



    def test_greet(self):
        """
        Testar att funktionen "greet" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["1", "marvin1"]
        self.norepr = True
        self._multi_arguments = ["dbwebb är bäst"]
        self.check_print_contain(self._multi_arguments, ["dbwebb är bäst"], marvin.greet)



    def test_temperature_high(self):
        """
        Testar att funktionen "celcius_to_farenheit" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["2", "marvin1"]
        self.norepr = True
        self._multi_arguments = ["70"]
        self.check_print_contain(self._multi_arguments, ["158.0"], marvin.celcius_to_farenheit)



    def test_word_manipulation(self):
        """
        Testar att funktionen "word_manipulation" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["3", "marvin1"]
        word, times = "to the moon", 10
        self.norepr = True
        self._multi_arguments = [word, times]

        # If the studend does not include newlines in output.
        try:
            self.check_print_contain(self._multi_arguments, [(word + "\n") * times], marvin.word_manipulation)
        except AssertionError as _:
            self.check_print_contain(self._multi_arguments, [word * times], marvin.word_manipulation)



    def test_sum_and_avrage(self):
        """
        Testar att funktionen "sum_and_average" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["101", "25.4", "1", "7.16", "2.123"]
        sum_numbers = sum([float(n) for n in numbers])
        med_numbers = sum_numbers/len(numbers)

        self.tags = ["4", "marvin1"]
        self.norepr = True
        self._multi_arguments = [*numbers, "done"]

        self.check_print_contain(
            self._multi_arguments,
            [
                str(round(sum_numbers, 2)), str(round(med_numbers, 2))
            ],
            marvin.sum_and_average
        )



    def test_hyphen_string(self):
        """
        Testar att funktionen "hyphen_string" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["5", "marvin1"]
        self.norepr = True
        self._multi_arguments = ["python"]

        self.check_print_contain(
            self._multi_arguments,
            ["p-yy-ttt-hhhh-ooooo-nnnnnn"],
            marvin.hyphen_string
        )



    def test_is_isogram(self):
        """
        Testar att funktionen "is_isogram" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["6", "marvin1"]
        self.norepr = True
        self._multi_arguments = ["paris"]

        self.check_print_contain(
            self._multi_arguments,
            ["Match!"],
            marvin.is_isogram
        )



    def test_compare_numbers(self):
        """
        Testar att funktionen "compare_numbers" finns i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "12", "12", "12", "14"]

        self.tags = ["7", "marvin1"]
        self.norepr = True
        self._multi_arguments = [*numbers, "done"]

        self.check_print_contain(
            self._multi_arguments,
            ["larger!", "same!", "same!", "larger!"],
            marvin.compare_numbers
        )


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
