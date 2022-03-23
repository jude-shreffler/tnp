#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jude Shreffler"
__version__ = "0.0.0"
__license__ = "MIT"

import json

def main():
    """ Main entry point of the app """
    print("Parsing data\n")

    # open our file objects
    rawData = open("weball22.txt", "r")
    scrapedData = open("scrape.csv", "w")
    repCount = 0
    demCount = 0
    othCount = 0

    inString = rawData.read()

    rawList = inString.split('\n')

    for i in rawList:
        if i.find('|') != -1:
            j = i.split('|')
        #print(len(j))

        if j[4] == "DEM":
            demCount += 1
        elif j[4] == "REP":
            repCount += 1
        else:
            othCount += 1

    scrapedData.write(f"{repCount}\n{demCount}\n{othCount}\n")

    print(f"repCount: {repCount}")
    print(f"demCount: {demCount}")
    print(f"othCount: {othCount}")

    rawData.close()
    scrapedData.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()