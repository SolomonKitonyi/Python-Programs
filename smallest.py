#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:26:15 2020

@author: solomon
"""
smallest = ""
for i in [23,33,44,3,55,66,77,5]:
    if i < smallest:
        smallest = i
    print i,smallest
print "Smallest number is", smallest