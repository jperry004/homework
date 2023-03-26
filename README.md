# Complex Number Module

This module defines a ComplexNumber class that represents complex numbers with real and imaginary components. The class provides methods for basic arithmetic operations, such as addition, subtraction, multiplication, and division, as well as a string representation for displaying the complex number.

# Usage
To use the ComplexNumber class, simply import it into your Python code:

from complex_number import ComplexNumber

# Create a complex number
z = ComplexNumber(1, 2)

# Perform arithmetic operations
z1 = ComplexNumber(3, 4)

z2 = ComplexNumber(2, 1)

z3 = z1 + z2

# Testing
This module includes a set of unit tests for the ComplexNumber class, which can be found in the test_complex_number.py file. To run the tests, simply execute the test_complex_number.py file:


python test_complex_number.py

If all the tests pass, you should see a message indicating that all the tests passed. If any tests fail, the error message will indicate which test(s) failed and what the expected and actual values were.

# Requirements
This module requires Python 3.0 or higher, as well as the unittest module, which is included in the Python standard library.

# License
None
