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
    parser.add_argument('-mv', '--max_value', type=int, default=20,
                        help='Max Number of tries you want to play')
    parser.add_argument ('-umt', '--timed_game', action='store_true',
                         help = 'timed game mode')
    args = vars(parser.parse_args())
    print(args)

    maximum_tries = args['max_value']
    timed_game = args['timed_game']

    print('Get Prepared, the chalange is about to beggin...')

    if timed_game == False:
        Query_List = untimedGame(maximum_tries)
    else:
        Query_List = timedGame(maximum_tries)

    for query in Query_List:
        print(query.request + ' ' + query.response)


if __name__ == '__main__':
    main()
