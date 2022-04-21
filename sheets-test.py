#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jude Shreffler"
__version__ = "prototyping"
__license__ = "MIT"

import math
import pandas
import openpyxl # python threw a fit when i didnt include this. no clue what it does
                # pandas might rely on it
import numpy
import matplotlib as plot

# global constants for the column identifiers
AMOUNT = 17
INKIND_DESCRIPTION = 20

ROW_OFFSET = 3 # used when printing the name of a row. internally, the rows are labelled 0 through n, 
               # however in the original spreadsheet they're labeled m through n + m. ROW_OFFSET is

# TODO where do people around athens donate money? largest athens donors? money with a-county dems & a-county repubs?
#      how do independants get their money? organizations that funnel their money like go blue or win red?

def main():
    """ Main entry point of the app """

    #importing our excel sheet 
    df = pandas.read_excel("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) BLYSTONE CONTRIB - 1_31_22 .xlsx", header = 1)
    columns = df.values.T.tolist() # converts our dataframe to a list of columns
                                   # [[column1, data, ...], [column2, data, ...], ...]

    sum = 0
    iterations = 0
    
    for i in columns[AMOUNT]:
        if not pandas.isna(i):
            sum += i
        else:
            # put some shit here that takes care of the items that get bought and dont have an amount next to them
            # for now, just print the lines that have NaN
            # print(f"Row {iterations + ROW_OFFSET} is not a number, description is {columns[INKIND_DESCRIPTION][iterations]}")
            foo()

        iterations += 1

    print(f"Total amount contributed: ${sum}")

def foo():
    return numpy.void

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


