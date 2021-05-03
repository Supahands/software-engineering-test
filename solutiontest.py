import unittest
import datetime
from solution import getDatefromCleanedInputs
from solution import calculateLoginSummary
from solution import Login
from solution import printLoginSummaryAsTable
from unittest.mock import Mock


class TestSolution(unittest.TestCase):

    def testGetDatefromCleanedInputsHappyPath(self):
        """
        Test that getDatefromCleanedInputs() returns list of Date objects from DateTime-happy path
        """
        dateTimeList = ['2021-05-22 09:59:04', '2021-05-27 15:59:04',
                        '2021-06-24 04:59:04']
        date1 = datetime.date(2021, 5, 22)
        date2 = datetime.date(2021, 5, 27)
        date3 = datetime.date(2021, 6, 24)
        dateList = [date1, date2, date3]
        dateListResult = getDatefromCleanedInputs(dateTimeList)
        self.assertEqual(dateList, dateListResult)

    def testGetDatefromCleanedInputsWithDuplicates(self):
        """
        Test that getDatefromCleanedInputs() returns unique date list
        """
        dateTimeList = ['2021-05-22 09:59:04',
                        '2021-05-22 04:59:04']
        date1 = datetime.date(2021, 5, 22)
        dateList = [date1]
        dateListResult = getDatefromCleanedInputs(dateTimeList)
        self.assertEqual(dateList, dateListResult)

    def testGetDatefromCleanedInputsCheckResultIsSorted(self):
        """
        Test that getDatefromCleanedInputs() returns sorted list of date objects
        """
        dateTimeList = ['2021-05-22 09:59:04', '2021-05-27 15:59:04',
                        '2021-06-24 04:59:04']
        date1 = datetime.date(2021, 5, 22)
        date2 = datetime.date(2021, 5, 27)
        date3 = datetime.date(2021, 6, 24)
        dateList = [date1, date2, date3]
        dateListResult = getDatefromCleanedInputs(dateTimeList)
        self.assertEqual(dateList, dateListResult)

    def testGetDatefromCleanedInputsCheckEmptyInput(self):
        """
        Test that getDatefromCleanedInputs() returns empty result when no input is present
        """
        dateTimeList = []
        dateList = []
        dateListResult = getDatefromCleanedInputs(dateTimeList)
        self.assertEqual(dateList, dateListResult)

    def testCalculateLoginSummaryHappyPath(self):
        """
        Test that calculateLoginSummary function happy path
        """
        date1 = datetime.date(2021, 5, 22)
        date2 = datetime.date(2021, 5, 27)
        date3 = datetime.date(2021, 6, 24)
        dateList = [date1, date2, date3]

        consecutiveDayCountList = []
        loginObj1 = Login(date1, date1, 1)
        loginObj2 = Login(date2, date2, 1)
        loginObj3 = Login(date3, date3, 1)
        consecutiveDayCountList = [loginObj1, loginObj2, loginObj3]
        consecutiveDayCountListResult = calculateLoginSummary(dateList)
        self.assertListEqual(consecutiveDayCountList,
                             consecutiveDayCountListResult)

    def testCalculateLoginSummaryCheckCount(self):
        """
        Test that calculateLoginSummary function checks for count values correctness
        """
        date1 = datetime.date(2021, 5, 22)
        date2 = datetime.date(2021, 5, 23)
        date3 = datetime.date(2021, 5, 24)
        date4 = datetime.date(2021, 5, 28)

        dateList = [date1, date2, date3, date4]

        consecutiveDayCountList = []
        loginObj1 = Login(date1, date3, 3)
        loginObj2 = Login(date4, date4, 1)
        consecutiveDayCountList = [loginObj1, loginObj2]
        consecutiveDayCountListResult = calculateLoginSummary(dateList)
        self.assertListEqual(consecutiveDayCountList,
                             consecutiveDayCountListResult)

    def testCalculateLoginSummaryCheckSummaryCountConsecutiveDaysCrossingAMonth(self):
        """
        Test that calculateLoginSummary function calculates count correctly when 
        consecutive days crossing months are passed
        """
        date1 = datetime.date(2021, 5, 30)
        date2 = datetime.date(2021, 5, 31)
        date3 = datetime.date(2021, 6, 1)
        date4 = datetime.date(2021, 6, 2)
        dateList = [date1, date2, date3, date4]

        consecutiveDayCountList = []
        loginObj1 = Login(date1, date4, 4)
        consecutiveDayCountList = [loginObj1]
        consecutiveDayCountListResult = calculateLoginSummary(dateList)
        self.assertListEqual(consecutiveDayCountList,
                             consecutiveDayCountListResult)

    def testPrintLoginSummaryAsTableForDecresingOrderOfLoginCounts(self):
        """
        Test that the login count summary is reverse sorted, mocking the print and tabulate calls here
        """
        date1 = datetime.date(2021, 5, 30)
        date2 = datetime.date(2021, 5, 31)
        date3 = datetime.date(2021, 6, 5)
        date4 = datetime.date(2021, 6, 8)

        consecutiveDayCountList = []
        loginObj1 = Login(date1, date2, 2)
        loginObj2 = Login(date3, date3, 1)
        loginObj3 = Login(date4, date4, 1)

        consecutiveDayCountList = [loginObj2, loginObj1, loginObj3]
        consecutiveDayCountSorted = [loginObj1, loginObj2, loginObj3]

        Mock().print()
        Mock().tabulate()

        printLoginSummaryAsTable(consecutiveDayCountList)
        self.assertListEqual(consecutiveDayCountList,
                             consecutiveDayCountSorted)


if __name__ == '__main__':
    unittest.main()
