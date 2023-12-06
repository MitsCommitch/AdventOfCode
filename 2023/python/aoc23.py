import argparse
from datetime import datetime as dt
import os
import re
import sys

def init_arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('day')

    return parser

def main(argv):
    parser = init_arg_parse()
    args = parser.parse_args()

    with open(f'./day_{args.day}/input.txt') as f:
        input = f.read().splitlines()

    match args.day:
        case '01':
            from day_01 import day01
            day01.main(input)

        case '02':
            from day_02 import day02
            day02.main(input)
        case _:
            return
        


if __name__ == "__main__":
    main(sys.argv)