#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os, unittest

class Tests():   
    """ Class which create a series of unitary tests from the current working
    directory
    """

    def suite(self): 
        """ Function which stores all the modules to be tested """
        # Look for the file which contain the unitary tests
        modules_to_test = []
        test_dir = os.listdir('.')
        for test in test_dir:
            if test.startswith('test') and test.endswith('.py'):
                modules_to_test.append(test.rstrip('.py'))
        # Creation of the unittest TestSuite
        alltests = unittest.TestSuite()
        for module in map(__import__, modules_to_test):
            module.testvars = ["variables you want to pass through"]
            alltests.addTest(unittest.findTestCases(module))
        return alltests

if __name__ == '__main__':
    MyTests = Tests()
    unittest.main(defaultTest='MyTests.suite')
