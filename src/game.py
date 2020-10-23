import random
import readchar
from time import time
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
