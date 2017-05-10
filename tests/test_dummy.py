import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):
    def calculation_should_pass1(self):
        weekday = calculate(2017, 5, 10)
        self.assertEqual(weekday, 2)

        retcode = main(("--year", "2017", "--month", "5", "--day", "10"))
        self.assertEqual(retcode, 2)

    def calculation_should_pass2(self):
        weekday = calculate(2014, 1, 1)
        self.assertEqual(weekday, 2)

        retcode = main(("--year", "2014", "--month", "1", "--day", "1"))
        self.assertEqual(retcode, 2)

    def calculation_should_fail_wrong_date(self):
        weekday = calculate(2013, 2, 29)
        self.assertEqual(weekday, 4)

        retcode = main(("--year", "2013", "--month", "2", "--day", "29"))
        self.assertEqual(retcode, 4)

    def calculation_should_fail_wrong_match(self):
        weekday = calculate(2013, 2, 1)
        self.assertEqual(weekday, 3)

        retcode = main(("--year", "2013", "--month", "2", "--day", "1"))
        self.assertEqual(retcode, 4)

    def calculation_should_fail_out_of_date(self):
        weekday = calculate(2010, 5, 32)
        self.assertEqual(weekday, 1)

        retcode = main(("--year", "2010", "--month", "5", "--day", "32"))
        self.assertEqual(retcode, 1)

    def calculation_should_fail_wrong_arguments(self):
        weekday = calculate(2017, 5, 10)
        self.assertEqual(weekday, 2)

        retcode = main(("--year", "2010", "--monh", "5", "--day", "32"))
        self.assertEqual(retcode, 1)

    def calculation_should_fail_wrong_weekday(self):
        weekday = calculate(2017, 5, -1)
        self.assertEqual(weekday, 2)

    def calculation_should_fail_wrong_month(self):
        weekday = calculate(2017, -5, 10)
        self.assertEqual(weekday, 2)

    def calculation_should_test_leap_year(self):
        weekday = calculate(1996, 3, 1)
        self.assertEqual(weekday, 4)

        retcode = main(("--year", "1996", "--month", "3", "--day", "1"))
        self.assertEqual(retcode, 4)


if __name__ == '__main__':
    unittest.main()
