#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author = syst1m


import sys 

PYVERSION = sys.version.split()[0]

if PYVERSION <= "3":
    exit("[CRITICAL] incompatible Python version detected ('%s'). "
         "For successfully running this project, you'll have to use version 3"
         "(visit 'http://www.python.org/download/')" % PYVERSION)