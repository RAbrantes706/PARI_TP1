import random

class Query:
    def __init__(self):
        self.request = random.randint(ord('a'), ord('z'))

    def ask(self):
        