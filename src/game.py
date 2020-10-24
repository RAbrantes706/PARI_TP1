import random
import readchar
from time import time, localtime
from colorama import Fore

class Query: #Create a Class responsable for the logic of the game
    def __init__(self):
        self.request = chr(random.randint(ord('a'), ord('z'))) #self.request is a random char in a range ok "a" to "z"

    def ask(self): #Ask is responsable to store information about the question, aswer and time spended
        print('Type letter: ' + Fore.BLUE + self.request + Fore.RESET)

        start = time()
        self.response = readchar.readchar()
        self.time = time() - start #Time spended to aswer the question

        print('You typed letter:'),
        if self.response.lower() == self.request: #If the user get it right
            self.correct = True
            print(Fore.GREEN + self.response.lower() + Fore.RESET)
        else:
            self.correct = False #If the user get it wrong
            print(Fore.RED + self.response.lower() + Fore.RESET)

        if self.response == ' ':
            return -1
        else:
            return 0

    def __str__(self): #Define how to print the class when calls str(Query)
        return 'I asked ' + self.request + ' and you input '\
               + self.response + ' in ' + self.time + ' seconds'

def timedGame(maxTime): #Creating a function to run the logic of Query.ask in a while loop for timed game
    print('Running test up to ' + str(maxTime) + ' seconds.')
    print('Press any key to start...') #Print instructions and settings for the user
    readchar.readchar() #Hold until the user type any key
    startDate = time() #setting a relative time comparision

    queryList = [] #Create store variable to hold information about the game (Class Query)
    givenUp = False #Create a boolean to set user desistent

    start = time() #setting a relative time comparision
    while time() - start < maxTime and not givenUp: #While the max time is not reached and the user have not give up
        query = Query() #Create a Query Class to suport the function
        givenUp = query.ask() != 0 #Run the question and set if the user gived up
        if time() - start < maxTime: #if time is not expired
            queryList.append(query) #append the answer to the list
        else: #if time is expired
            print('The last input was out of time!') #Show the last typing was out of time

    endDate = time() #Close the time referency
    return (queryList, startDate, endDate) #Return data of each question, the start date and end date to main function

def untimedGame(maxAttempts): #Creating a function to run the logic of Query.ask in a for loop for untimed game
    print('Running test up to ' + str(maxAttempts) + ' attempts.')
    print('Press any key to start...') #Print instructions and settings for the user
    readchar.readchar() #Hold until the user type any key
    startDate = time() #setting a relative time comparision

    queryList = [] #Create store variable to hold information about the game (Class Query)
    for i in range(0, maxAttempts): #Run the Query.ask in a for loop
        query = Query()
        givenUp = query.ask() != 0
        if(givenUp):
            break
        queryList.append(query)

    endDate = time() #Close the time referency
    return (queryList, startDate, endDate) #Return data of each question, the start date and end date to main function
