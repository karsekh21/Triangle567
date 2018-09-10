# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return('InvalidInput')

    if a <= 0 or b <= 0 or c <= 0:
        return('InvalidInput')

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return('InvalidInput')

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if not(a >= (c-b)) or not(b >= (c-a)) or not(c <= (a + b)):
        return('NotATriangle')
    else:
    # now we know that we have a valid triangle
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return('Right')
        elif a != b and b != c and a != c:
            return('Scalene')
        elif a==b and b==c:
            return('Equilateral')
        elif a==b or b==c or c==a:
            return('Isoceles')
    
    """
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return ('InvalidInput')

    if a <= 0 or b <= 0 or c <= 0:
        return ('InvalidInput')

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return ('InvalidInput')

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (c-b)) or (b >= (c-a)) or (c <= (a + b)):
        return ('NotATriangle')

    # now we know that we have a valid triangle
    if a == b and b == a:
            return ('Equilateral')
    elif ((a * 2) + (b * 2)) == (c * 2):
            return ('Right')
    elif (a != b) and  (b != c) and (a != b):
            return ('Scalene')
    else:
            return ('Isoceles')"""
