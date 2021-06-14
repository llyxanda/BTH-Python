#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import re
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


class Test2Marvin2NewMenus(ExamTestCase):
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



    def test_randomize_string_menu(self):
        """
        Testar att anropa menyval 8 via main funktionen i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande sträng finns med i utskrift fast med bokstäverna i annan ordning:
        {correct}
        Fick följande:
        {student}
        """
        string = "Borde inte bli samma igen"
        self.tags = ["8", "marvin2"]
        self._multi_arguments = ["8", string, "", "q"]

        arguments = set(self.USER_TAGS)
        if arguments:
            test_case_tags = set(self.tags)
            if not arguments.intersection(test_case_tags):
                raise unittest.SkipTest("Inkluderar inte någon av de givna taggarna")


        with patch("builtins.input", side_effect=self._multi_arguments):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()

        length = len(string)
        pattern = fr"{string} --> ([{string}]{{{length}}})"

        self.student_answer = repr(str_data)
        self.correct_answer = repr(string)


        try:
            rnd_str = re.search(pattern, str_data)[1]
        except TypeError:
            raise AssertionError
        if string == rnd_str or sorted(string) != sorted(rnd_str):
            raise AssertionError



    def test_randomize_string_func(self):
        """
        Testar att anropa randomize_string via marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande sträng finns med i utskrift fast med bokstäverna i annan ordning:
        {correct}
        Fick följande:
        {student}
        """
        string = "MedSiffror1234567890"
        self.tags = ["8", "marvin2"]
        self._multi_arguments = [string]

        arguments = set(self.USER_TAGS)
        if arguments:
            test_case_tags = set(self.tags)
            if not arguments.intersection(test_case_tags):
                raise unittest.SkipTest("Inkluderar inte någon av de givna taggarna")


        with patch("builtins.input", side_effect=self._multi_arguments):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                marvin.randomize_string()
                str_data = fake_out.getvalue()

        length = len(string)
        pattern = fr"{string} --> ([{string}]{{{length}}})"

        self.student_answer = str_data
        self.correct_answer = repr(string)

        try:
            rnd_str = re.search(pattern, str_data)[1]
        except TypeError:
            raise AssertionError
        if string == rnd_str or sorted(string) != sorted(rnd_str):
            raise AssertionError



    def test_get_acronym_menu(self):
        """
        Testar att anropa menyval 9 via main funktionen i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["9", "marvin2"]
        self.norepr = True
        self._multi_arguments = ["9", "BRöderna Ivarsson Osby", "", "q"]
        self.check_print_contain(
            self._multi_arguments,
            ["BRIO"],
            main.main
        )



    def test_get_acronym_func(self):
        """
        Testar att anropa funktionen get_acronym i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["9", "marvin2"]
        self._argument = ["Ingvar Kamprad Elmtaryd Agunnaryd"]
        self.check_print_contain(
            self._argument,
            ["IKEA"],
            marvin.get_acronym
        )



    def test_mask_string_menu(self):
        """
        Testar att anropa menyval 10 via main funktionen i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["10", "marvin2"]
        self.norepr = True
        self._multi_arguments = ["10", "4556364607935616", "", "q"]
        self.check_print_contain(
            self._multi_arguments,
            ["############5616"],
            main.main
        )



    def test_mask_string_func(self):
        """
        Testar att anropa funktionen mask_string i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["10", "marvin2"]
        self._argument = ["Hej Hej"]
        self.check_print_contain(
            self._argument,
            ["### Hej"],
            marvin.mask_string
        )



    def test_multiply_str_func(self):
        """
        Testar att anropa funktionen multiply_str i marvin.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["10", "3", "marvin2"]
        self._multi_arguments = ["#", 5]
        res = marvin.multiply_str(*self._multi_arguments)
        self.assertEqual("#####", res)



if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
