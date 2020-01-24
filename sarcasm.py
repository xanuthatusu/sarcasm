#!/usr/bin/env python3
import random
import pyperclip
import argparse

def formatMessage(args):
    setupCLI()
    sarcastic = ""

    for word in args.message.split(" "):
        for char in word:
            cap = random.randrange(2)
            if cap == 0:
                sarcastic += char.lower()
            else:
                sarcastic += char.upper()
        sarcastic += " "

    if args.output:
        print(sarcastic)

    if args.copy:
        pyperclip.copy(sarcastic)

def setupCLI():
    parser = argparse.ArgumentParser(description="Format text to a sARcaStIc FoNT.")
    parser.add_argument("message", type=str, help="The message you want to format")
    parser.add_argument("-c", "--copy", dest="copy", action="store_true", help="Copy output to clipboard")
    parser.add_argument("-s", "--silent", dest="output", action="store_false", help="Silence output to std out")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    import sys
    args = setupCLI()
    formatMessage(args)
