import random
import readchar
from time import time, localtime
from colorama import Fore

class Query:
    def __init__(self):
        self.request = chr(random.randint(ord('a'), ord('z')))

    def ask(self):
        print('Type letter: ' + Fore.BLUE + self.request + Fore.RESET)

        start = time()
        self.response = readchar.readchar()
        self.time = time() - start

        print('You typed letter:'),
        if self.response.lower() == self.request:
            self.correct = True
            print(Fore.GREEN + self.response.lower() + Fore.RESET)
        else:
            self.correct = False
            print(Fore.RED + self.response.lower() + Fore.RESET)

        if self.response == ' ':
            return -1
        else:
            return 0

    def __str__(self):
        return 'I asked ' + self.request + ' and you input '\
               + self.response + ' in ' + self.time + ' seconds'

def timedGame(maxTime):
    print('Running test up to ' + str(maxTime) + ' seconds.')
    print('Press any key to start...')
    readchar.readchar()
    startDate = time()

    queryList = []
    givenUp = False

    start = time()
    while time() - start < maxTime and not givenUp:
        query = Query()
        givenUp = query.ask() != 0
        if time() - start < maxTime:
            queryList.append(query)
        else:
            print('The last input was out of time!')

    endDate = time()
    return (queryList, startDate, endDate)

def untimedGame(maxAttempts):
    print('Running test up to ' + str(maxAttempts) + ' attempts.')
    print('Press any key to start...')
    readchar.readchar()
    startDate = time()

    queryList = []
    for i in range(0, maxAttempts):
        query = Query()
        givenUp = query.ask() != 0
        if(givenUp):
            break
        queryList.append(query)

    endDate = time()
    return (queryList, startDate, endDate)
