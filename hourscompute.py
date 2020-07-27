#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:50:12 2020

@author: solomon
"""

inp = raw_input("Enter hours: ");
hours = float(inp);
inp = raw_input ("Enter rate: ");
rate = float(inp);
#print hours, rate;
pay = rate * hours;
print pay;