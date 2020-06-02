#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:56:29 2020

@author: solomon
"""

while True:
    line = raw_input(">")
    if line[0] == "#":
     continue
    if line == "Done":
     break
    print line
print "Hey hey"