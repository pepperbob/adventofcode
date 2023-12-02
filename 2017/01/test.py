import unittest
from solve import solveIt, solveIt2

class TestSum(unittest.TestCase):

    def test_solve0(self):
        self.assertEqual(solveIt("1122"), 3, "Should be 3")

    def test_solve1(self):
        self.assertEqual(solveIt("1111"), 4, "Should be 4")

    def test_solve2(self):
        self.assertEqual(solveIt("1234"), 0, "Should be 0")

    def test_solve3(self):
        self.assertEqual(solveIt("91212129"), 9, "Should be 9")

    def test_solve10(self):
        self.assertEqual(solveIt2("1212"), 6, "Should be 3")

    def test_solve11(self):
        self.assertEqual(solveIt2("1221"), 0, "Should be 4")

    def test_solve12(self):
        self.assertEqual(solveIt2("123425"), 4, "Should be 0")

    def test_solve13(self):
        self.assertEqual(solveIt2("123123"), 12, "Should be 9")

    def test_solve14(self):
        self.assertEqual(solveIt2("12131415"), 4, "Should be 9")





if __name__ == '__main__':
    unittest.main()
