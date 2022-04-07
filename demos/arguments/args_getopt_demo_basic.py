import getopt
import sys

"""
Ce module est destiné à illustrer le comportement de getopt. Pour un exemple,
voir le module getopt_usage
"""

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hvi:o:',
                               ['help', 'verbose', 'input=', 'output='])
except getopt.GetoptError as err:
    print(str(err))
    sys.exit(2)

for option, argument in opts:
    print(option + ":" + argument)
print("-----")
for argument in args:
    print(argument)