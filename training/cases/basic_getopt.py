#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Démonstration de l'utilisation de getopt

Usage:
    basic_getopt options

Options:
  * -h or --help: displays help
  * -o or --output [file]: displays the file intended for output
"""

from __future__ import absolute_import, print_function
import getopt, sys


def usage():
    """
    Print the usage. Prints the module doc for convenience.

    :return: None
    """
    print(__doc__)


def main():
    """
    Code executed when module is called as main.

    :return: None
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ho:', ['help', 'output='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-o', '--output'):
            print('Output is %s' % a)

    print(args)


if __name__ == '__main__':
    main()
