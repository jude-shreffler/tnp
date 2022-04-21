#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jude Shreffler"
__version__ = "0.1.0"
__license__ = "MIT"

import TopDonor

def main():
    TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) BLYSTONE CONTRIB - 1_31_22 .xlsx", False)
    #TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) CRANLEY CONTRIB - 2_16_22 .xlsx")
    #TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) RENACCI - 1_31_22 .xlsx")
    #TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) WHALEY CONTRIB - 2_12_22 .xlsx")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()