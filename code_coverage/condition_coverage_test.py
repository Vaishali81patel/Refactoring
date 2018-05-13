import demo2

import unittest


class ConditionCoverageTests(unittest.TestCase):
    """
    http://istqbexamcertification.com/what-is-condition-coverage/

    100% condition covered
    """
    def setUp(self):
        print("A test case is called.")

    def test_1(self):
        """
        100%/3 condition covered
        """
        self.assertEqual(10, demo2.method1(5, True, True, True, False))

    def test_2(self):
        """
        100%/3 condition covered
        """
        self.assertEqual(9, demo2.method1(5, True, False, False, True))

    def test_3(self):
        """
        100%/3 condition covered
        """
        self.assertEqual(10, demo2.method1(5, False, True, False, False))

    def tearDown(self):
        print("This test case is done!")

if __name__ == '__main__':
    unittest.main(verbosity=2)