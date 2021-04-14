import unittest
from datetime import datetime
from solution import consecCounter
from solution import toDates

class TestConsec(unittest.TestCase):
    # if length = end-start
    # if sorted descending
    # if date conversion worked (string to date)
    # if date repeated 
    # leap year test
    # crossing the boundry to next month
    def test_date_conversion(self):
        # Test if date conversion works accurately
        data = ['2021-06-03 10:11:07', '2021-05-30 18:11:07']
        expected = [datetime(2021,6,3),datetime(2021,5,30)]
        result = toDates(data)
        self.assertEqual(result,expected)

    def test_length(self):
        # To test if the number of consecutive days is correct
        data = [datetime(2021,6,3,0,0), datetime(2021,6,4,0,0), datetime(2021,6,5,0,0), datetime(2021,1,5,0,0)]
        expected = [['2021-06-03','2021-06-05', 3]]
        result = consecCounter(data)
        self.assertEqual(result,expected)

    
    def test_multiple_length(self):
        # To test if there are multiple different consecutive logins 
        data = [datetime(2021,3,3,0,0),datetime(2021,4,3,0,0),datetime(2021,5,3,0,0)]
        expected = [['2021-03-03','2021-03-03', 1],['2021-04-03','2021-04-03', 1]]
        result = consecCounter(data)
        self.assertEqual(result,expected)


    def test_sort(self):
        # Test to see if it sorts the 
        data = [datetime(2021,3,3,0,0),datetime(2021,3,4,0,0),datetime(2021,3,5,0,0),datetime(2021,3,6,0,0),
        datetime(2021,4,3,0,0),datetime(2021,4,4,0,0),datetime(2021,4,5,0,0), 
        datetime(2021,5,3),datetime(2021,5,4),datetime(2021,5,4)]
        expected = [['2021-03-03','2021-03-06', 4],
        ['2021-04-03','2021-04-05', 3],
        ['2021-05-03','2021-05-04', 2]]
        
        result = consecCounter(data)
        self.assertEqual(result,expected)

    def test_date_repeat(self):
        data = [datetime(2021,3,3),datetime(2021,3,3)]
        expected = [['2021-03-03','2021-03-03', 1]]
        result = consecCounter(data)
        self.assertEqual(result,expected)

    def test_leap_year(self):
        data = [datetime(2020,2,29),datetime(2020,2,29)]
        expected = [['2020-02-29','2020-02-29', 1]]
        result = consecCounter(data)
        self.assertEqual(result,expected)




if __name__ == '__main__':
    unittest.main()
    print("Everything passed")