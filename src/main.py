#!/usr/bin/python
#
# -----------------------------------------------
# Typing test main script.
#
# PARI - TP1 - GRUPO 3, October 2020
# -----------------------------------------------

from game import Query

def main():
    for i in range(0,10):
        q = Query()
        q.ask()

if __name__ == '__main__':
    main()
