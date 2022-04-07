"""
Illustration de l'utilisation de getopt

Usage:
    getopt_usage options

Options:
  * -h or --help: displays help
  * -v or --verbose: verbose mode
  * -o or --output [file]: displays the file intended for output
"""

import getopt
import sys


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
        opts, args = getopt.getopt(sys.argv[1:], 'hvo:', ['help', 'verbose', 'output='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    print(type(opts))

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-o', '--output'):
            output_filename = a
            print('Output is %s' % output_filename)

    print(args)


if __name__ == '__main__':
    main()
