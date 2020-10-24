#!/usr/bin/python
#
# -----------------------------------------------
# Typing test main script.
#
# PARI - TP1 - GRUPO 3, October 2020
# -----------------------------------------------


import argparse
from colorama import Fore
from game import timedGame, untimedGame #Import functions from "game.py"
from collections import namedtuple
from time import ctime
from pprint import pprint

Input = namedtuple('Input', ['requested', 'received', 'duration']) #Create a Tuple wich will recieve all data of each try in the game

def main():

    parser = argparse.ArgumentParser(description=Fore.YELLOW + 'Test of Texting Skills. I chalange YOU, to type the maximum of correct chars you can.' + Fore.GREEN) #Create a Parse to the script

    parser.add_argument ('-umt', '--timed_game', action='store_true',
                         help = Fore.RED + 'Activate Timed game mode' + Fore.YELLOW + ', if you select it, the Max Number you tipped will become the max duration of the challenge' + Fore.GREEN)

    parser.add_argument('-mv', '--max_value', type=int, default=20,  #Adding Parses
                        help= Fore.YELLOW + 'Max Number of tries you want in ' + Fore.RED + 'untimed game mode'
                        + Fore.BLUE + ' OR' + Fore.YELLOW + ' Max seconds you want to play in' + Fore.RED + ' untimed game mode'+ Fore.RESET +
                        "\n" + Fore.CYAN + '\n Default = 20 ' + Fore.RESET)

    args = vars(parser.parse_args()) #Create a Variable to keep information of parser input
    print(args) #Show to the user the type of game with the number of tries or seconds of duration

    maximum_tries = args['max_value'] #Create an integer Variable to hold information about the max value inputed
    timed_game = args['timed_game'] #Create a boolean Variable to set into "timed" and "untimed" game modes.

    print('Get Prepared, the chalange is about to beggin... (You will fail)') #Print a challenging message to scary the user

    if not timed_game: #This "if" function must indicate which game mode should be runned
        Query_List = untimedGame(maximum_tries) #Select untimed mode type and set the maximun duration for "maximun_tries" second
    else:
        Query_List = timedGame(maximum_tries) #Select timed mode type and set the maximun tries for "maximun_tries"

    hits = 0  #Setting global control variables
    hit_total_duration = 0
    miss_total_duration = 0
    inputs = []
    for query in Query_List[0]: #Stock every data about each try of the user
        inputs.append(Input(query.request, query.response, query.time))
        if query.correct: #Check if the user was sucessfull and count the time spended
            hits += 1
            hit_total_duration += query.time  #If he typed it right
        else:
            miss_total_duration += query.time #Or wrong

    #Starting to process the information getted in the user chalange (He failed, of course)
    accuracy = 0 #Creating Global Variables
    type_average_duration = 0
    type_miss_average_duration = 0
    type_hit_average_duration = 0
    if not hits == len(Query_List[0]): #Avoiding future erros
        type_miss_average_duration = miss_total_duration/(len(Query_List[0])-hits)
    if not hits == 0: #Avoiding future erros
        type_hit_average_duration = hit_total_duration/hits
    if not len(Query_List[0]) == 0: #Avoiding future erros
        accuracy = hits*1.0/len(Query_List[0])
        type_average_duration = (Query_List[2] - Query_List[1]) / len(Query_List[0])

    stats = {'inputs':inputs, #Create a Dictionary with all information processed of the Challange
             'test_duration':Query_List[2]-Query_List[1],
             'test_start':ctime(Query_List[1]),
             'test_end':ctime(Query_List[2]),
             'number_of_types':len(Query_List[0]),
             'number_of_hits':hits,
             'accuracy':accuracy,
             'type_average_duration':type_average_duration,
             'type_hit_average_duration':type_hit_average_duration,
             'type_miss_average_duration':type_miss_average_duration}

    pprint(stats) #Pretty Print it !!

if __name__ == '__main__':
    main()
