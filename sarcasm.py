#!/usr/local/bin/python3
import random

def formatMessage(message):
    sarcastic = ""
    for word in message.split(" "):
        for char in word:
            cap = random.randrange(2)
            if cap == 0:
                sarcastic += char.lower()
            else:
                sarcastic += char.upper()
        sarcastic += " "
    print(sarcastic)

if __name__ == "__main__":
    import sys
    formatMessage(sys.argv[1])
