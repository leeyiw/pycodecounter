#!/usr/bin/env python

import sys
import os

suffixes = ('.c', '.cpp', '.h', '.py')
fullnames = ('Makefile', 'makefile')

def pycodecounter_help():
    print 'Usage: pycodecount.py PATH'

def count_code(code_file):
    nlines = 0
    f = open(code_path + '/' + code_file, 'r')
    for line in f:
        nlines += 1;
    print "%s: %d" % (code_file, nlines)
    return nlines

def is_code_file(filename):
    for fullname in fullnames:
        if fullname == filename:
            return True

    root, ext = os.path.splitext(filename)
    for suffix in suffixes:
        if suffix == ext:
            return True

    return False

if len(sys.argv) != 2:
    pycodecounter_help()
    sys.exit(2)

code_path = sys.argv[1]
nlines = 0
if os.path.isdir(code_path):
    for root, dirs, files in os.walk(code_path):
        for f in files:
            fullpath = os.path.join(root, f)
            if is_code_file(f):
                nlines += count_code(fullpath)
else:
    nlines = count_code(code_path)

print "Total: %d" % (nlines)
