"""
Illustration de l'usage de `argparse` afin d'exploiter les arguments du
lancement de programme.

Le module est destiné à illustrer la présentation, si vous voulez le tester,
décommantez les lignes sauf celles commentées `will fail`.

.. seealso:: Voir https://docs.python.org/3/howto/argparse.html
"""

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This script does something.")

    # parser.add_argument('who', help='Who are you ?')
    # parser.add_argument('many', type=int)
    # parser.add_argument("command", help="Action this program should perform")
    # parser.add_argument("command", choices=["run", "load", "update"],
    #                     help="Action this program should perform")
    # parser.add_argument('-v', '--verbose') # Will fail
    # parser.add_argument('-v', '--verbose', action='store_true')
    # parser.add_argument('-o', "--output",
    #                     help="Output file name")
    #
    args = parser.parse_args()

    # if args.verbose:
    #     print('lets do it')
    #
    # print(args.command)
    #
    #
    # if args.output:
    #     print("output file: " + args.output)
    #
    # for i in range(args.many):
    #     print("Hello " + args.who)
