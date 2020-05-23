#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:37:17 2020

@author: solomon
"""

def greet(kind):
 try:
    if kind == 1:
        return "Hello "
    elif kind == 2:
        return "Bonjur "
    else:
        return "Good to see you "
 except:
        print "Ooop!!! error"
        
print greet(1), 'Solomon'
print greet(2),"Nick"
print greet(10),"Lorna"
