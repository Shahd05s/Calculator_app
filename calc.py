#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:43:22 2025

@author: sultanalobaid
"""

import math

class Mathematics:
    # Functions for basic operations
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    # Functions for trigonometric operations
    def sine(self, a):
        return math.sin(math.radians(a))  # Convert degrees to radians

    def cosine(self, a):
        return math.cos(math.radians(a))  # Convert degrees to radians

    def tangent(self, a):
        return math.tan(math.radians(a))  # Convert degrees to radians

    # Functions for inverse trigonometric operations
    def arcsine(self, a):
        return math.degrees(math.asin(a))  # Convert result from radians to degrees

    def arccos(self, a):
        return math.degrees(math.acos(a))  # Convert result from radians to degrees

    def arctan(self, a):
        return math.degrees(math.atan(a))  # Convert result from radians to degrees

    # Functions for other operations
    def square(self, a):
        return a ** 2

    def square_root(self, a):
        return math.sqrt(a)

    def pi(self):
        return math.pi
