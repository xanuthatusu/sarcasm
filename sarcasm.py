#!/usr/local/bin/python3
import random

def formatMessage(message):
    sarcastic = ""
    for word in message.split(" "):
        for char in word:
            cap = random.randrange(2)
            if cap == 0:
                print(char.lower(), end='')
            else:
                print(char.upper(), end='')
        print(" ", end='')

if __name__ == "__main__":
    import sys
    formatMessage(sys.argv[1])
