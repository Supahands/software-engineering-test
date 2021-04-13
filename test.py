import unittest
import solution as sol
from datetime import datetime


class TestSolution(unittest.TestCase):

    def test_sortTimeStamps(self):
        """Test for sorting string similar to seed output."""
        # Test includes dates with same month but diff day(date 3 and 5 with 1)
        # same month and day,(date 3 and 5)
        # and diff month but same day (date 2 and 3)
        # and diff month and day (date 4)
        timestamps = "['2021-03-19 23:13:05', '2021-05-18 08:13:05', " + \
        "'2021-03-18 07:13:05', '2021-04-11 08:13:05', '2021-03-18 08:13:05']"
        result = sol.sortTimeStamps(timestamps)
        date1 = datetime.strptime('2021-03-19 23:13:05', "%Y-%m-%d %H:%M:%S")
        date2 = datetime.strptime('2021-05-18 08:13:05', "%Y-%m-%d %H:%M:%S")
        date3 = datetime.strptime('2021-03-18 07:13:05', "%Y-%m-%d %H:%M:%S")
        date4 = datetime.strptime('2021-04-11 08:13:05', "%Y-%m-%d %H:%M:%S")
        date5 = datetime.strptime('2021-03-18 08:13:05', "%Y-%m-%d %H:%M:%S")
        expected = [date3, date5, date1, date4, date2]
        self.assertEqual(result, expected)

    def test_getConsecDates(self):
        # Test includes sequence of 3 timestamps over 2 days (date3 - 5)
        # Two consecutive dates (date1 - 2)
        # Three seperate single time stamps, at the start(date0), middle(date7) and end(date6)
        date0 = datetime.strptime('2021-02-17 07:13:05', "%Y-%m-%d %H:%M:%S")
        date1 = datetime.strptime('2021-03-19 23:13:05', "%Y-%m-%d %H:%M:%S")
        date2 = datetime.strptime('2021-03-20 07:13:05', "%Y-%m-%d %H:%M:%S")
        date7 = datetime.strptime('2021-04-01 07:13:05', "%Y-%m-%d %H:%M:%S")
        date3 = datetime.strptime('2021-04-21 23:13:05', "%Y-%m-%d %H:%M:%S")
        date4 = datetime.strptime('2021-04-22 07:13:05', "%Y-%m-%d %H:%M:%S")
        date5 = datetime.strptime('2021-04-22 23:13:05', "%Y-%m-%d %H:%M:%S")
        date6 = datetime.strptime('2021-04-27 07:13:05', "%Y-%m-%d %H:%M:%S")
        tsl = [date0, date1, date2, date7, date3, date4, date5, date6]
        result = sol.getConsecDates(tsl)
        expected = [[date1.date(), date2.date(), 2], [date3.date(), date5.date(), 2],
                    [date0.date(), date0.date(), 1], [date7.date(), date7.date(), 1],
                    [date6.date(), date6.date(), 1]]
        self.assertEqual(result, expected)

    def test_datesToTable(self):
        # Test data includes rows with 3,2 and 1 consective days
        date1 = datetime.strptime('2021-03-19 23:13:05', "%Y-%m-%d %H:%M:%S")
        date2 = datetime.strptime('2021-03-20 07:13:05', "%Y-%m-%d %H:%M:%S")
        date3 = datetime.strptime('2021-04-21 23:13:05', "%Y-%m-%d %H:%M:%S")
        date5 = datetime.strptime('2021-04-23 23:13:05', "%Y-%m-%d %H:%M:%S")
        date6 = datetime.strptime('2021-04-27 07:13:05', "%Y-%m-%d %H:%M:%S")
        consecDates = [[date3.date(), date5.date(), 3], [date1.date(), date2.date(), 2],
                       [date6.date(), date6.date(), 1]]
        result = sol.datesToTable(consecDates)
        expectedStr = "START" + " " * 7 + "END" + " " * 11 + "LENGTH\n"
        expectedStr += "-" * 10 + "  " + "-" * 10 + "  " + "-" * 8 + "\n"
        expectedStr += '2021-04-21' + "  " + '2021-04-23' + " " * 9 + "3\n"
        expectedStr += '2021-03-19' + "  " + '2021-03-20' + " " * 9 + "2\n"
        expectedStr += '2021-04-27' + "  " + '2021-04-27' + " " * 9 + "1"
        self.assertEqual(result, expectedStr)


if __name__ == '__main__':
    unittest.main()
