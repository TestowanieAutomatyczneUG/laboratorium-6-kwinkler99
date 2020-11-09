class FizzBuzz:
    def game(self, num):
        """Takes a number and returns a string depending on the divisibility of the number
        >>> c = FizzBuzz()
        >>> c.game(15)
        'FizzBuzz'
        >>> c.game(9)
        'Fizz'
        >>> c.game(55)
        'Buzz'
        >>> c.game("20")
        Traceback (most recent call last):
          File "/snap/pycharm-professional/218/plugins/python/helpers/pycharm/docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest game[4]>", line 1, in <module>
            c.game("20")
          File "/home/kasia/inf/Testowanie/laboratorium-6-kwinkler99/FizzBuzz.py", line 45, in game
            raise ValueError("Error! It isn't integer")
        ValueError: Error! It isn't integer
        >>> c.game(30.40)
        Traceback (most recent call last):
          File "/snap/pycharm-professional/218/plugins/python/helpers/pycharm/docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest game[5]>", line 1, in <module>
            c.game(30.40)
          File "/home/kasia/inf/Testowanie/laboratorium-6-kwinkler99/FizzBuzz.py", line 47, in game
            raise ValueError("Error! It isn't integer")
        ValueError: Error! It isn't integer
        >>> c.game()
        Traceback (most recent call last):
          File "/snap/pycharm-professional/218/plugins/python/helpers/pycharm/docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest game[6]>", line 1, in <module>
            c.game()
        TypeError: game() missing 1 required positional argument: 'num'
        >>> c.game(1)
        Traceback (most recent call last):
          File "/snap/pycharm-professional/218/plugins/python/helpers/pycharm/docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest FizzBuzz.game[7]>", line 1, in <module>
            c.game(1)
          File "/home/kasia/inf/Testowanie/laboratorium-6-kwinkler99/FizzBuzz.py", line 47, in game
            raise Exception("Error!")
        Exception: Error!
        """
        if type(num) == int:
            if (num % 15) == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 == 0:
                return "Buzz"
            else:
                raise Exception("Error!")
        else:
            raise ValueError("Error! It isn't integer")





if __name__ == "__main__":

    import doctest
    doctest.testmod(extraglobs={'c': FizzBuzz()})
