#!/usr/bin/python
#
# -----------------------------------------------
# Typing test main script.
#
# PARI - TP1 - GRUPO 3, October 2020
# -----------------------------------------------
import argparse

import readchar

from game import Query, timedGame, untimedGame

def main():

    parser = argparse.ArgumentParser(description='Test of Texting Skills')
    parser.add_argument('-mt', '--max_tries', type=int, default=20,
                        help='Max Number to test')
    args = vars(parser.parse_args())
    print(args)

    maximum_tries = args['max_tries']
    print('Get Prepared, the chalange is about to beggin...')

    Query_List = untimedGame(maximum_tries)

    for query in Query_List:
        print(query.request + ' ' + query.response)


if __name__ == '__main__':
    main()
