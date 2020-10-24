import random
import readchar
from time import time
from colorama import Fore


class Query:
    """
    Class that holds information of one attempt on the game.
    Upon construction a random character is generated to request the user.
    """
    def __init__(self):
        self.request = chr(random.randint(ord('a'), ord('z')))  # self.request is a random char in a range ok "a" to "z"
        self.response = chr(0)
        self.time = 0
        self.correct = False

    def ask(self):
        """
        Ask the user to input the requested character.
        :return: 0 if the user input was normal, -1 if the user wants to give up.
        """
        print('Type letter: ' + Fore.BLUE + self.request + Fore.RESET)

        start = time()
        self.response = readchar.readchar()
        self.time = time() - start  # Time spent to answer the question

        print('You typed letter:'),
        if self.response.lower() == self.request:  # If the user get it right
            self.correct = True
            print(Fore.GREEN + self.response.lower() + Fore.RESET)
        else:
            self.correct = False  # If the user get it wrong
            print(Fore.RED + self.response.lower() + Fore.RESET)

        if self.response == ' ':
            return -1
        else:
            return 0

    def __str__(self):  # Define how to print the class when calls str(Query)
        return 'I asked ' + self.request + ' and you input ' + self.response + ' in ' + str(self.time) + ' seconds'


def timedGame(maxTime):  # Creating a function to run the logic of Query.ask in a while loop for timed game
    """
    Execute a game that runs during a given time.
    :param maxTime: Time that the user has to play the game.
    :return: Tuple that contains (list of queries, start time, end time)
    """
    print('Running test up to ' + str(maxTime) + ' seconds.')
    print('Press any key to start...')  # Print instructions and settings for the user
    readchar.readchar()  # Hold until the user type any key

    queryList = []  # Create list to hold information about the game (Class Query)
    givenUp = False  # Create a variable to check if the user gives up

    startDate = time()  # Save the time of the start
    while time() - startDate < maxTime and not givenUp:  # While the max time is not reached and the user have not
                                                         # give up
        query = Query()  # Create a Query Class to support the function
        givenUp = query.ask() != 0  # Run the question and check if the user has given up
        if time() - startDate < maxTime:  # if time is not expired
            queryList.append(query)  # append the answer to the list
        else:  # if time has expired
            print('The last input was out of time!')  # Show that the last typing was out of time

    endDate = time()  # Close the time reference
    return (queryList, startDate, endDate)  # Return data of each question, the start date and end date to main function


def untimedGame(maxAttempts):  # Creating a function to run the logic of Query.ask in a for loop for untimed game
    """
    Execute a game that runs during a given time.
    :param maxAttempts: Number of attempts that the user has during the game.
    :return: Tuple that contains (list of queries, start time, end time).
    """
    print('Running test up to ' + str(maxAttempts) + ' attempts.')
    print('Press any key to start...')  # Print instructions and settings for the user
    readchar.readchar()  # Hold until the user type any key
    startDate = time()  # setting a relative time comparison

    queryList = []  # Create store variable to hold information about the game (Class Query)
    for i in range(0, maxAttempts):  # Run the Query.ask in a for loop
        query = Query()
        givenUp = query.ask() != 0
        if (givenUp):
            break
        queryList.append(query)

    endDate = time()  # Close the time reference
    return (queryList, startDate, endDate)  # Return data of each question, the start date and end date to main function
