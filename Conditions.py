#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:28:30 2020

@author: solomon
"""

num = raw_input("Enter a number you would like to know the colour it holds ")
if num < 10:
    print "The number holds a bright colour"
elif (num > 10 and num <= 50) :
    print "The number holds a shouting colour"
else:
    print "The number hold a very dull colour"