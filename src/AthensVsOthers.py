#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jude Shreffler"
__version__ = "0.1.0"
__license__ = "MIT"

#import math
import pandas
#import openpyxl
#import numpy
import matplotlib.pyplot as plot

# global constants for the column identifiers
#FIRST_NAME = 6
#LAST_NAME = 8
COUNTY = 15
AMOUNT = 17

def run(fileName):
    #importing our excel sheet 
    df = pandas.read_excel(fileName, header = 1)
    columns = df.values.T.tolist()

    total = 0
    dTotal = 0
    # get the amounts from athens added up
    for i in range(len(columns[AMOUNT])):
        # county and amount import, with NaN protection on the amount
        county = str(columns[COUNTY][i])


        if pandas.isna(columns[AMOUNT][i]):
            amount = 0
        else:
            amount = int(columns[AMOUNT][i])

        # format it to 5 digits
        if len(county) == 6:
            # remove the comma
            county.split(",")
            temp = ""
            for i in county:
                temp += i
            county = temp
        elif len(county) > 6:
            # remove everything after the first five digits
            county[0:5]

        # add amount to total if county is athens
        if county == "45701":
            total += amount
            dTotal += 1

    # print the info we got
    print(f"{amount} donated from athens county, in {dTotal} donations.")

    """
    # make the pie chart
    fig, ax = plot.subplots()
    ax.pie(cleanAmountList, explode=explode, labels=cleanDonorList, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #plot.show()

    fileName = fileName.split("\\")
    candidateName =  fileName[len(fileName) - 1].split()
    candidateName = candidateName[1]
    fileName = candidateName + "-top-donor" + ("-othersTrue" if includeOthers else "") + ".png"

    plot.savefig(fileName)
    """