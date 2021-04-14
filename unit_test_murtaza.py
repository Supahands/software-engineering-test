import unittest
import solution_murtaza
from datetime import datetime

# Please comment the last line of solution_murtaza.py before running the unit test suite
# If the line is not commented, all the tests will fail as the script will run for seed.py by default


class TestSolution(unittest.TestCase):
    def test_convert_string_to_date_lst(self):
        lst = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05',
               '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05',
               '2021-03-18 15:13:05']
        date_lst = [datetime.strptime('2021-03-13 15:13:05', '%Y-%m-%d %H:%M:%S').date(),
                    datetime.strptime('2021-03-16 15:13:05', '%Y-%m-%d %H:%M:%S').date(),
                    datetime.strptime('2021-03-17 07:13:05', '%Y-%m-%d %H:%M:%S').date(),
                    datetime.strptime('2021-03-18 07:13:05', '%Y-%m-%d %H:%M:%S').date()]
        self.assertEqual(solution_murtaza.convert_string_to_date_lst(lst), date_lst)

    def test_derive_streaks(self):
        # Checking test case in program requirements
        date_list_1 = solution_murtaza.convert_string_to_date_lst(['2021-03-13 15:13:05', '2021-03-13 23:13:05',
                                                                   '2021-03-16 15:13:05', '2021-03-16 23:13:05',
                                                                   '2021-03-17 07:13:05', '2021-03-17 15:13:05',
                                                                   '2021-03-17 23:13:05', '2021-03-18 07:13:05',
                                                                   '2021-03-18 15:13:05'])
        result1 = [('2021-03-13', '2021-03-13', 1), ('2021-03-16', '2021-03-18', 3)]

        self.assertEqual(solution_murtaza.derive_streaks(date_list_1), result1)

        # Checking empty list
        date_list_2 = []
        self.assertEqual(solution_murtaza.derive_streaks(date_list_2), [])

        # Checking list with all entries in series
        date_list_3 = solution_murtaza.convert_string_to_date_lst(['2021-03-13 15:13:05', '2021-03-13 23:13:05',
                                                                   '2021-03-14 16:13:24', '2021-03-15 13:12:41',
                                                                   '2021-03-16 15:13:05', '2021-03-16 23:13:05',
                                                                   '2021-03-17 07:13:05', '2021-03-17 15:13:05',
                                                                   '2021-03-17 23:13:05', '2021-03-18 07:13:05',
                                                                   '2021-03-18 15:13:05'])
        result3 = [('2021-03-13', '2021-03-18', 6)]
        self.assertEqual(solution_murtaza.derive_streaks(date_list_3), result3)

        # Checking list with no entries in series
        date_list_4 = solution_murtaza.convert_string_to_date_lst(['2021-03-19 15:13:05', '2021-03-11 23:13:05',
                                                                   '2021-03-01 16:13:24', '2021-03-09 13:12:41',
                                                                   '2021-03-15 15:13:05', '2021-03-04 23:13:05',
                                                                   '2021-03-30 07:13:05', '2021-03-25 15:13:05',
                                                                   '2021-03-07 23:13:05', '2021-04-18 07:13:05',
                                                                   '2021-10-18 15:13:05'])
        result4 = [('2021-03-01', '2021-03-01', 1),
                   ('2021-03-04', '2021-03-04', 1),
                   ('2021-03-07', '2021-03-07', 1),
                   ('2021-03-09', '2021-03-09', 1),
                   ('2021-03-11', '2021-03-11', 1),
                   ('2021-03-15', '2021-03-15', 1),
                   ('2021-03-19', '2021-03-19', 1),
                   ('2021-03-25', '2021-03-25', 1),
                   ('2021-03-30', '2021-03-30', 1),
                   ('2021-04-18', '2021-04-18', 1),
                   ('2021-10-18', '2021-10-18', 1)]

        self.assertEqual(solution_murtaza.derive_streaks(date_list_4), result4)


if __name__ == '__main__':
    unittest.main()
