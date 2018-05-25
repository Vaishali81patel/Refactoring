"""
Unit Testing with Python
http://www.drdobbs.com/testing/unit-testing-with-python/240165163?pgno=1

https://docs.python.org/3/library/unittest.html
"""

from unit_test_file_handler import *
from unit_test_employee import *
from unit_test_data import *

import unittest
# import doctest

def unit_suite():
    theSuite = unittest.TestSuite()
    # '''
    # suite1.addTest(FooTests1("test_one"))
    # suite1.addTest(FooTests1("test_two"))
    # suite1.addTest(FooTests1("test_hello_world"))
    # suite1.addTest(FooTests2("test_three"))
    # '''
    theSuite.addTest(unittest.makeSuite(EmployeeDataFormatTests))
    theSuite.addTest(unittest.makeSuite(FileHandlerTests))
    theSuite.addTest(unittest.makeSuite(EmployeeUnitTests))
    return theSuite


if __name__ == '__main__':
    runner_unit = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = unit_suite()
    runner_unit.run(test_suite)
