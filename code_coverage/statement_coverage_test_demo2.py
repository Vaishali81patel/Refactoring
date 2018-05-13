import demo2

import unittest


class StatementCoverageTests(unittest.TestCase):
    def setUp(self):
        print("A test case is called.")

    def test_1(self):
        """
        100% statement covered
        """
        self.assertEqual(10, demo2.method1(5, True, True, True, False))

    def tearDown(self):
        print("This test case is done!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
