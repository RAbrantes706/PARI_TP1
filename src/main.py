#!/usr/bin/python
#
# -----------------------------------------------
# Typing test main script.
#
# PARI - TP1 - GRUPO 3, October 2020
# -----------------------------------------------
import argparse

import readchar

from game import Query

Query_List = []

def main():

    parser = argparse.ArgumentParser(description='Test of Texting Skills')
    parser.add_argument('-mt', '--max_tries', type=int, default=20,
                        help='Max Number to test')
    args = vars(parser.parse_args())
    print(args)

    maximum_tries = args['max_tries']
    print('Get Prepared, the chalange is about to beggin, you will type ' + str(maximum_tries) + ' chars in a range of "a" to "z" ')
    print('press any key to continue')
    readchar.readchar()

    for i in range(0,maximum_tries):
        q = Query()
        q.ask()
        Query_List.append(q)


if __name__ == '__main__':
    main()
