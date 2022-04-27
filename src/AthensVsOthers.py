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

def formatName(name):
    temp = ""
    i = 0
    while i < len(name):
        if i == 0 or name[i - 1] == " ":
            temp += name[i].upper()
        else:
            temp += name[i].lower()
        i += 1

    return temp

def run(files):
    #importing our excel sheet

    # these two need to go in all functions
    count = 0
    labels = []

    # data arrays
    total = []
    totalFromAthens = []
    dTotal = []

    for fileName in files:
        # deciding which columns to look at
        race = fileName.split("/")[2]
        if race == "attorney-race":
            COUNTY = 8
            AMOUNT = 12
            HEAD = 2
        elif race == "sec-of-state-race":
            COUNTY = 8
            AMOUNT = 12
            HEAD = 2
        elif race == "treasurer-race":
            COUNTY = 8
            AMOUNT = 12
            HEAD = 1
        elif race == "auditor-race":
            if fileName.split("/")[3] == "keith-faber":
                COUNTY = 15
                AMOUNT = 17
            elif fileName.split("/")[3] == "taylor-sappington":
                COUNTY = 8
                AMOUNT = 12
            HEAD = 1
        elif race == "gov-races":
            COUNTY = 15
            AMOUNT = 17
            HEAD = 2
        elif race == "sen-races":
            COUNTY = 25
            AMOUNT = 35
            HEAD = 1
        elif race == "house-races":
            COUNTY = 8
            AMOUNT = 12
            HEAD = 1
        
        #actually reading the file
        df = pandas.read_excel(fileName, header = HEAD)
        columns = df.values.T.tolist() #makes an array of the spreadsheet

        #building the labels
        fileName = fileName.split("/")
        labels.append(fileName[3].split("-"))   
        labels[count] = labels[count][1]
        labels[count] = formatName(labels[count])

        #setting up our data arrays
        total.append(0)
        totalFromAthens.append(0)
        dTotal.append(0)

        # get the amounts from athens added up
        for i in range(len(columns[AMOUNT])):

            # county and amount import, with NaN protection on the amount
            county = str(columns[COUNTY][i])

            if pandas.isna(columns[AMOUNT][i]):
                amount = 0
            else:
                amount = str(columns[AMOUNT][i])

                if amount[0] == "$": # remove $ if it has one
                    amount = amount[1:len(amount)]
                
                amount = amount.split(",")
                temp = ""
                for i in amount:
                    temp += i
                amount = temp

                amount = float(amount)

            # format it to 5 digits if it's longer than that
            if len(county) > 5:
                county = county[0:5]

            # add amount to total if county is athens
            if county == "45701":
                totalFromAthens[count] += amount
                dTotal[count] += 1

            total[count] += amount

        count += 1

    # make the stacked bar chart
    fig, ax = plot.subplots()
    ax.bar(labels, totalFromAthens, 0.35, label = "Money from Athens")

    ax.set_ylabel("Amount Donated")
    ax.set_title("Amounts Donated from Athens")
    ax.legend()

    # file name, change the subdirectory of out
    fileName = "../out/donations-from-athens/"
    for file in files:
        fileName += file.split("/")[3]
        fileName += "-vs-"

    fileName = fileName[0:len(fileName) - 4]

    plot.savefig(fileName)