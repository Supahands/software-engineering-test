import unittest
import doctest
import solution


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(solution))
    return tests
