#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:47:37 2020

@author: solomon
"""

largest = 0
for num in [12,23,45,67,89,899,2,1234]:
    if num > largest:
        largest = num
        print "The largest number is ",largest
    print largest
print "Done The largest number is ", largest