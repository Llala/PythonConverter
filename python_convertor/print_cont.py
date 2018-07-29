# coding=utf-8

import sys
import os

print ('Number of arguments:', len(sys.argv), 'arguments.')
if len(sys.argv) < 3:
    print (" Syntax: print_cont.py arg[1]:file path arg[2]:file name")
else:
    path = sys.argv[1]
    name = sys.argv[2]
    full_path = path+ '/' +name
    f= open(full_path, 'r+')
    line = f.read()
    print('---------------------Contents listing------------------------------------------')
    while line:
        if not line: break
        print(line)
        line = f.read()
