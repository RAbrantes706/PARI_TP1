#!/usr/bin/python
#
# -----------------------------------------------
# Typing test main script.
#
# PARI - TP1 - GRUPO 3, October 2020
# -----------------------------------------------

import argparse
from game import timedGame, untimedGame
from collections import namedtuple
from time import ctime
from pprint import pprint

Input = namedtuple('Input', ['requested', 'received', 'duration'])

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

    if not timed_game:
        Query_List = untimedGame(maximum_tries)
    else:
        Query_List = timedGame(maximum_tries)

    hits = 0
    hit_total_duration = 0
    miss_total_duration = 0
    inputs = []
    for query in Query_List[0]:
        inputs.append(Input(query.request, query.response, query.time))
        if query.correct:
            hits += 1
            hit_total_duration += query.time
        else:
            miss_total_duration += query.time

    accuracy = 0
    type_average_duration = 0
    type_miss_average_duration = 0
    type_hit_average_duration = 0
    if not hits == len(Query_List[0]):
        type_miss_average_duration = miss_total_duration/(len(Query_List[0])-hits)
    if not hits == 0:
        type_hit_average_duration = hit_total_duration/hits
    if not len(Query_List[0]) == 0:
        accuracy = hits*1.0/len(Query_List[0])
        type_average_duration = (Query_List[2] - Query_List[1]) / len(Query_List[0])

    stats = {'inputs':inputs,
             'test_duration':Query_List[2]-Query_List[1],
             'test_start':ctime(Query_List[1]),
             'test_end':ctime(Query_List[2]),
             'number_of_types':len(Query_List[0]),
             'number_of_hits':hits,
             'accuracy':accuracy,
             'type_average_duration':type_average_duration,
             'type_hit_average_duration':type_hit_average_duration,
             'type_miss_average_duration':type_miss_average_duration}

    pprint(stats)
if __name__ == '__main__':
    main()
