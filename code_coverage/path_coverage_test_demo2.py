import demo2

import unittest


class PathCoverageTests(unittest.TestCase):
    """
    http://testersthoughtsuncombed.blogspot.co.nz/2013/02/statement-coverage-vs-branch-coverage.html

    100% path covered
    """
    def setUp(self):
        print("A test case is called.")

    def test_1(self):
        """
        100%/4 path covered
        """
        self.assertEqual(10, demo2.method1(5, True, True, True, False))

    def test_2(self):
        """
        100%/4 path covered
        """
        self.assertEqual(11, demo2.method1(5, True, True, False, False))

    def test_3(self):
        """
        100%/4 path covered
        """
        self.assertEqual(9, demo2.method1(5, False, True, True, False))

    def test_4(self):
        """
        100%/4 path covered
        """
        self.assertEqual(10, demo2.method1(5, False, True, False, False))

    def tearDown(self):
        print("This test case is done!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
