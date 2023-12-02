import unittest
from solve import solveIt, solveIt2

class TestSum(unittest.TestCase):
    
    def test01(self):
        input=["5 1 9 5", "7 5 3", "2 4 6 8"]

        assert solveIt(input) == 18, "Checksum should be 18"

    def test01(self):
        input=["5 9 2 8", "9 4 7 3", "3 8 6 5"]

        assert solveIt2(input) == 9, "Checksum should be 9"

if __name__ == '__main__':
    unittest.main()
