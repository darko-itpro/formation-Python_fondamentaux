#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""Voir https://docs.python.org/3/howto/argparse.html"""

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="This program requires a file path to open some file.")
    parser.add_argument("file_path", help="Path to the file to load", type=str)
    parser.add_argument("-v", "--verbose", help="Activate output", action="store_true")

    args = parser.parse_args()

    if args.verbose:
        print("Ok, I will talk")

    print(args.file_path)
