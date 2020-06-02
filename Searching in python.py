#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:08:47 2020

@author: solomon
"""

Is_there= False

for value in [12,39,34,45,39,67,78,39,39]:
    if value == 39:
        Is_there = True
        break
    print value,Is_there
print Is_there