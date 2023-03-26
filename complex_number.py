#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines a `ComplexNumber` class that represents complex numbers 
with real and imaginary components. The class provides methods for basic 
arithmetic operations, such as addition, subtraction, multiplication, 
and division, as well as a string representation for displaying 
the complex number.

Written by Josh Perry for Qblox
"""


class ComplexNumber:
    def __init__(self, real, imag):
        # Initialize the complex number with a real and imaginary component
        # TODO: Implement exception handling for inputs and "others". 
        
        self.real = real
        self.imag = imag

    def __str__(self):
        # Format the complex number as a string
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        # Add two complex numbers
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Subtract two complex numbers
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # Multiply two complex numbers
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        # Divide two complex numbers
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)
    
    # TODO: Implement absolute value and equivalence dunder methods. 