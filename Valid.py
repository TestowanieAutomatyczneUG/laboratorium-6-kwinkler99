import unittest
import string


class Valid:
    def ValidPassword(self, password):
        """Takes a number and returns a string depending on the divisibility of the number
        >>> c = Valid()
        >>> c.ValidPassword("acdefgijklmn")
        False
        >>> c.ValidPassword("aassd42pql")
        False
        >>> c.ValidPassword("_123asasdadd")
        False
        >>> c.ValidPassword("1Ab_")
        False
        >>> c.ValidPassword("")
        False
        >>> c.ValidPassword("Adas_adsdy656")
        True
        >>> c.ValidPassword("abcd efgh23_=")
        False
        >>> c.ValidPassword("Ad_"+345)
        Traceback (most recent call last):
          File "/snap/pycharm-professional/218/plugins/python/helpers/pycharm/docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest Valid.Valid.ValidPassword[6]>", line 1, in <module>
            c.ValidPassword("Ad_"+345)
        TypeError: can only concatenate str (not "int") to str

        >>> c.ValidPassword(1234)
        Traceback (most recent call last):
          File "/snap/pycharm-professional/218/plugins/python/helpers/pycharm/docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest Valid.Valid.ValidPassword[8]>", line 1, in <module>
            c.ValidPassword(1234)
          File "/home/kasia/inf/Testowanie/laboratorium-6-kwinkler99/Valid.py", line 57, in ValidPassword
            raise Exception("Error!")
        Exception: Error!
        """

        if type(password) == str:
            test = 0

            length = 0
            for letter in password:
                if letter.isalpha():
                    length += 1

            if length <= 8:
                return False

            for letter in password:
                if letter.isupper():
                    test += 1
                    break

            for number in password:
                if number.isdigit():
                    test += 1
                    break

            special_chars = string.punctuation
            bools = list(map(lambda char: char in special_chars, password))
            test += 1 if any(bools) else test

            if test == 3:
                return True
            else:
                return False
        else:
            raise Exception("Error!")


class ValidTest(unittest.TestCase):
    def setUp(self):
        self.temp = Valid()

    def test_8(self):
        self.assertEqual(self.temp.ValidPassword("1Ab_"), False)

    def test_capital_letter_without_num(self):
        self.assertEqual(self.temp.ValidPassword("asdD_adsad"), False)

    def test_capital_letter_with_num(self):
        self.assertEqual(self.temp.ValidPassword("asdD_adDs4ad"), True)

    def test_capital_letter(self):
        self.assertEqual(self.temp.ValidPassword("asdDASASDd"), False)

    def test_number_without_capital_letter(self):
        self.assertEqual(self.temp.ValidPassword("asd234-+d"), False)

    def test_number_without_special(self):
        self.assertEqual(self.temp.ValidPassword("as23Dd"), False)

    def test_number(self):
        self.assertEqual(self.temp.ValidPassword("req123_-plmdDjk"), True)

    def test_special_character(self):
        self.assertEqual(self.temp.ValidPassword("+-'/."), False)

    def test_special_character_true(self):
        self.assertEqual(self.temp.ValidPassword("A+-bgopdasd='/.5"), True)

    def test_using_space(self):
        self.assertEqual(self.temp.ValidPassword("abcd efgh23_="), False)

    def test_exception(self):
        self.assertRaises(Exception, self.temp.ValidPassword, 745)

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': Valid()})
