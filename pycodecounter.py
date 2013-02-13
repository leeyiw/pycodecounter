#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, getopt

suffixes = ['.c', '.cpp', '.h', '.py']
fullnames = ['Makefile', 'makefile']

def pycodecounter_help():
    print \
'''Usage: pycodecount.py [OPTION] PATH

Options:
  -l, --list      Print list of code file suffixes and full names
  -h, --help      Print this help message'''

def list_code_file_type():
    print 'Suffixes:',
    for s in suffixes:
        print s,
    print
    print 'Fullnames:',
    for f in fullnames:
        print f,
    print

def count_code(code_file):
    nlines = 0
    f = open(code_file, 'r')
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

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'lh', ['list', 'help'])
    except getopt.GetoptError as err:
       print err
       pycodecounter_help()
       sys.exit(2)

    for o, a in opts:
        if o in ('-l', '--list'):
            list_code_file_type()
            sys.exit()
        if o in ('-h', '--help'):
            pycodecounter_help()
            sys.exit()

    if len(args) != 1:
        pycodecounter_help()
        sys.exit(2)

    code_path = args[0]
    nlines = 0
    if os.path.isdir(code_path):
        for root, dirs, files in os.walk(code_path):
            for f in files:
                fullpath = os.path.join(root, f)
                if not os.path.samefile(code_path, '.'):
                    fullpath = os.path.join(code_path, fullpath)
                if is_code_file(f):
                    nlines += count_code(fullpath)
    else:
        nlines = count_code(code_path)

    print "Total: %d" % (nlines)

if __name__ == '__main__':
    main()
