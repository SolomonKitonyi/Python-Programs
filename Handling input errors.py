#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:36:59 2020

@author: solomon
"""

num = raw_input("Enter how year of birth")
try:
  age = 2020 -int(num)
  print "Your age is ",age
 
  if int(num) <= 2020:
    print "Great your input was as required"
  elif int(num) > 2020:
    print "Why lie your year of birth is not ",num
except:
    print "Error please input a number not a string"