import unittest

from datetime import datetime, timedelta
from random import shuffle

from solution import get_consecutive_date_ranges, process_output_date

class TestSolution(unittest.TestCase):

    def test_process_output_date(self):
        """
        Test that it can process output date string
        """
        today = datetime.today().date()
        result = process_output_date("'[" + today.strftime("%Y-%m-%d %H:%M:%S") + "']")
        self.assertEqual(result, today)

    def test_get_consecutive_date_ranges(self):
        """
        Test that it can get consecutive date ranges
        """
        today = datetime.today().date()
        num_days = 7

        dates = [today - timedelta(days=day) for day in range(num_days)]
        inconsecutive_date = today + timedelta(days=3)
        dates.append(inconsecutive_date)
        shuffle(dates)

        result = get_consecutive_date_ranges(dates)
        self.assertEqual(result, [
            (today - timedelta(days=num_days - 1), today, num_days),
            (inconsecutive_date, inconsecutive_date, 1)
        ])

if __name__ == '__main__':
    unittest.main()