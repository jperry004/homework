#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file includes a set of unit tests for the `ComplexNumber` class 
defined in `complex_number.py`. The tests cover the basic arithmetic 
operations, including addition, subtraction, multiplication, and division, 
as well as the string representation of a complex number. The tests use the 
Python `unittest` module to create test cases and check the expected results 
against the actual results. Running this file with 
`python test_complex_number.py` will execute the tests and 
report any failures or errors.

Written by Josh Perry for Qblox

"""

import unittest
from complex_number import ComplexNumber

class TestComplexNumber(unittest.TestCase):
    # TODO: Add negative tests to check exception handling
    
    def test_string_representation(self):
        # Test string representation of a complex number
        z = ComplexNumber(1, 2)
        result = str(z)
        expected = "1 + 2i"
        self.assertEqual(result, expected)

    def test_addition(self):
        # Test addition of two complex numbers
        z1 = ComplexNumber(1, 2)
        z2 = ComplexNumber(3, 4)
        result = z1 + z2
        expected = ComplexNumber(4, 6)
        self.assertEqual(result.real, expected.real)
        self.assertEqual(result.imag, expected.imag)

    def test_subtraction(self):
        # Test subtraction of two complex numbers
        z1 = ComplexNumber(1, 2)
        z2 = ComplexNumber(3, 4)
        result = z1 - z2
        expected = ComplexNumber(-2, -2)
        self.assertEqual(result.real, expected.real)
        self.assertEqual(result.imag, expected.imag)

    def test_multiplication(self):
        # Test multiplication of two complex numbers
        z1 = ComplexNumber(1, 2)
        z2 = ComplexNumber(3, 4)
        result = z1 * z2
        expected = ComplexNumber(-5, 10)
        self.assertEqual(result.real, expected.real)
        self.assertEqual(result.imag, expected.imag)

    def test_division(self):
        # Test division of two complex numbers
        z1 = ComplexNumber(1, 2)
        z2 = ComplexNumber(3, 4)
        result = z1 / z2
        expected = ComplexNumber(0.44, 0.08)
        self.assertAlmostEqual(result.real, expected.real)
        self.assertAlmostEqual(result.imag, expected.imag)

if __name__ == '__main__':
    unittest.main()
