#!/usr/bin/python
#
# -----------------------------------------------
# Typing test main script.
#
# PARI - TP1 - GRUPO 3, October 2020
# -----------------------------------------------

import argparse
from colorama import Fore
from game import timedGame, untimedGame  # Import functions from "game.py"
from collections import namedtuple
from time import ctime
from pprint import pprint

# Create a Tuple which will receive all data of each try in the game
Input = namedtuple('Input', ['requested', 'received', 'duration'])


def main():
    # Create a parser to the script
    parser = argparse.ArgumentParser(description=Fore.YELLOW + 'Test of Texting Skills. I challenge YOU, to type the ma'
                                     'ximum of correct chars you can.' + Fore.GREEN)

    parser.add_argument('-umt', '--timed_game', action='store_true',
                        help=Fore.RED + 'Activate Timed game mode' + Fore.YELLOW + ', if you select it, the Max Number'
                        ' you tipped will become the max duration of the challenge' + Fore.GREEN)

    parser.add_argument('-mv', '--max_value', type=int, default=20,
                        help=Fore.YELLOW + 'Max Number of tries you want in ' + Fore.RED + 'untimed game mode'
                             + Fore.BLUE + ' OR' + Fore.YELLOW + ' Max seconds you want to play in' + Fore.RED + ' tim'
                             'ed game mode' + Fore.RESET + "\n" + Fore.CYAN + '\n Default = 20 ' + Fore.RESET)

    args = vars(parser.parse_args())  # Create a Variable to keep information of parser input
    print(args)  # Show to the user the type of game with the number of tries or seconds of duration

    # Create an integer Variable to hold information about the max value inputted
    maximum_tries = args['max_value']
    # Create a boolean Variable to set into "timed" and "untimed" game modes.
    timed_game = args['timed_game']

    # Print a challenging message to scary the user
    print('Get Prepared, the challenge is about to begin... (You will fail)')

    # This "if" function must indicate which game mode should be ran
    if not timed_game:
        # Select timed mode type and set the maximum time to "maximum_tries"
        query_list = untimedGame(maximum_tries)
    else:
        # Select untimed mode type and set the maximum duration for "maximum_tries" second
        query_list = timedGame(maximum_tries)

    # Starting to process the information of the user challenge (He failed, of course)
    hits = 0
    hit_total_duration = 0
    miss_total_duration = 0
    inputs = []
    for query in query_list[0]:  # Stock every data about each try of the user
        inputs.append(Input(query.request, query.response, query.time))
        if query.correct:  # Check if the user was successful and count the time spent
            hits += 1
            hit_total_duration += query.time  # If he typed it right
        else:
            miss_total_duration += query.time  # Or wrong

    # Calculate some statistical data of the game
    accuracy = 0  # Creating Global Variables
    type_average_duration = 0
    type_miss_average_duration = 0
    type_hit_average_duration = 0
    if not hits == len(query_list[0]):  # Avoiding future errors
        type_miss_average_duration = miss_total_duration / (len(query_list[0]) - hits)
    if not hits == 0:  # Avoiding future errors
        type_hit_average_duration = hit_total_duration / hits
    if not len(query_list[0]) == 0:  # Avoiding future errors
        accuracy = hits * 1.0 / len(query_list[0])
        type_average_duration = (query_list[2] - query_list[1]) / len(query_list[0])

    # Create a Dictionary with all information processed of the Challenge
    stats = {'inputs': inputs,
             'test_duration': query_list[2] - query_list[1],
             'test_start': ctime(query_list[1]),
             'test_end': ctime(query_list[2]),
             'number_of_types': len(query_list[0]),
             'number_of_hits': hits,
             'accuracy': accuracy,
             'type_average_duration': type_average_duration,
             'type_hit_average_duration': type_hit_average_duration,
             'type_miss_average_duration': type_miss_average_duration}

    pprint(stats)  # Pretty Print it !!


if __name__ == '__main__':
    main()
