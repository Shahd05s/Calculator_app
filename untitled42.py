#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:29:02 2025

@author: sultanalobaid
"""

import math

# Create a class for mathematical operations
class Mathematics:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

    def sine(self, a):
        return math.sin(math.radians(a))  # Convert degrees to radians

    def cosine(self, a):
        return math.cos(math.radians(a))

    def tangent(self, a):
        return math.tan(math.radians(a))

    def arcsine(self, a):
        if -1 <= a <= 1:
            return math.degrees(math.asin(a))
        else:
            return "Input out of range"

    def arccos(self, a):
        if -1 <= a <= 1:
            return math.degrees(math.acos(a))
        else:
            return "Input out of range"

    def arctan(self, a):
        return math.degrees(math.atan(a))

    def square(self, a):
        return a ** 2

    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "Cannot take square root of a negative number"

    def pi(self):
        return math.pi