# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testIsATriangle(self):
        self.assertEqual(classifyTriangle(3,5,13), 'NotATriangle')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,3,4), 'Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(5,6,6), 'Isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(6,7,6), 'Isoceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2,6,8), 'Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(3,5,7), 'Scalene')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
