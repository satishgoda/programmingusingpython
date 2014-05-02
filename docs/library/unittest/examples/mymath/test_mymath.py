#!/usr/bin/env python

import unittest

import mymath


class Mod_mymath_Tests(unittest.TestCase):

    def test_add(self):
        result = mymath.add(2, 3)
        self.assertTrue(result is 5)

    def test_sub(self):
        result = mymath.sub(2, 3)
        self.assertTrue(result is -1)


if __name__ == '__main__':
    unittest.main()
