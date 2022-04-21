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
FIRST_NAME = 6
LAST_NAME = 8
AMOUNT = 17

def checkForValue(checkList, value):
    for i in range(len(checkList)):
        if checkList[i] == value:
            return i
    
    return -1

def indexLargest(aList, start):
    i = start
    largest = aList[i]
    largestIndex = i
    

    while i < len(aList):
        if aList[i] > largest:
            largest = aList[i]
            largestIndex = i
        i += 1
    
    return largestIndex

# primary is the list that will be sorted by, secondary will just get sorted as well
def sortLists(primary, secondary):
    i = 0
    while i < len(primary):
        j = indexLargest(primary, i)
        temp = primary[i]
        primary[i] = primary[j]
        primary[j] = temp

        temp = secondary[i]
        secondary[i] = secondary[j]
        secondary[j] = temp

        i += 1

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
        

def run(fileName, includeOthers):
    #importing our excel sheet 
    df = pandas.read_excel(fileName, header = 1)
    columns = df.values.T.tolist()

    donorList = [] # Name of every donor
    amountList = [] # Amount they donated
    donorName = ""
    inList = False

    # get the names and amounts into the lists
    for i in range(len(columns[AMOUNT])):

        # this block is our input guard on NaN
        if pandas.isna(columns[FIRST_NAME][i]) and pandas.isna(columns[LAST_NAME][i]):
            donorName = "ANONYMOUS"
        elif pandas.isna(columns[FIRST_NAME][i]) and not pandas.isna(columns[LAST_NAME][i]):
            donorName = str(columns[LAST_NAME][i])
        elif not pandas.isna(columns[FIRST_NAME][i]) and pandas.isna(columns[LAST_NAME][i]):
            donorName = str(columns[FIRST_NAME][i])
        else:
            donorName = str(columns[FIRST_NAME][i]) + " " + str(columns[LAST_NAME][i])

        # this puts them into the list, checking to see if they aleady have a "tab"
        inList = checkForValue(donorList, donorName)
        if inList >= 0:
            if not pandas.isna(columns[AMOUNT][i]):
                amountList[inList] += columns[AMOUNT][i]
        else:
            if not pandas.isna(columns[AMOUNT][i]):
                donorList.append(donorName)
                amountList.append(columns[AMOUNT][i])
    
    # sorts the list based on amountList
    sortLists(amountList, donorList)

    # fixes the all caps names
    i = 0
    while i < len(donorList):
        donorList[i] = formatName(donorList[i])
        i += 1

    # clean the data
    sum = amountList[0]
    i = 21
    while i < len(amountList):
        sum += amountList[i]
        i += 1

    """
    # print top 20 donors
    print("Top 20 donors and their donation amount in order:\r\n")
    for i in range(20):
        print(f"{i}: {donorList[i]} donated ${amountList[i]:.2f}")
    """

    cleanDonorList = []
    cleanAmountList = []
    explode = []
    i = 1
    while i < 21:
        cleanDonorList.append(donorList[i])
        cleanAmountList.append(amountList[i])
        explode.append(0)
        i += 1
    
    if includeOthers:
        cleanDonorList.append("Others")
        cleanAmountList.append(sum)
        explode.append(0.1)
    

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