import unittest
from my_script import *

class MyTestCase(unittest.TestCase):
    def test_startDate_lesser(self):
        for obj in result:
            self.assertLessEqual(obj.startDate, obj.endDate)

    def test_endDate_greater(self):
        for obj in result:
            self.assertGreaterEqual(obj.endDate, obj.startDate)

if __name__ == '__main__':
    unittest.main()
