#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jude Shreffler"
__version__ = "0.1.0"
__license__ = "MIT"

import time
import TopDonor
import AthensVsOthers as athens

def main():
    startTime = time.time()

    """ THESE NEED EDITED TO BE LINUX PATHS
    TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) BLYSTONE CONTRIB - 1_31_22 .xlsx", False)
    TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) CRANLEY CONTRIB - 2_16_22 .xlsx")
    TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) RENACCI - 1_31_22 .xlsx")
    TopDonor.run("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) WHALEY CONTRIB - 2_12_22 .xlsx")
    """

    athens.run(["../data/attorney-race/jeff-crossman/jeff-crossman-contributions-(4-21-22).xlsx", "../data/attorney-race/dave-yost/dave-yost-contributions-(4-21-22).xlsx"  ])
    athens.run(["../data/auditor-race/keith-faber/keith-faber-contributions-(2-16-22).xlsx", "../data/auditor-race/taylor-sappington/taylor-sappington-contributions-(3-31-22).xlsx"])
    athens.run(["../data/gov-races/jim-renacci/jim-renacci-contributions-(1-31-22).xlsx", "../data/gov-races/john-cranley/john-cranley-contributions-(2-16-22).xlsx", "../data/gov-races/mike-dewine/mike-dewine-contributions-(2-10-22).xlsx", "../data/gov-races/nan-whaley/nan-whaley-contributions-(2-12-22).xlsx"])
    athens.run(["../data/house-races/jay-edwards/jay-edwards-contributions-(3-31-22).xlsx", "../data/house-races/rhyan-goodman/rhyan-goodman-contributions-(4-26-22).xlsx"])
    athens.run(["../data/sec-of-state-race/chelsea-clark/chelsea-clark-contributions-(4-21-22).xlsx", "../data/sec-of-state-race/frank-larose/frank-larose-contributions-(4-21-22).xlsx", "../data/sec-of-state-race/john-adams/john-adams-contributions-(4-21-22).xlsx"])
    athens.run(["../data/sen-races/jane-timken/jane-timken-contributions-(4-21-22).xlsx", "../data/sen-races/jd-vance/jd-vance-contributions-(4-21-22).xlsx", "../data/sen-races/josh-mandel/josh-mandel-contributions-(4-21-22).xlsx", "../data/sen-races/mark-pukita/mark-pukita-contributions-(4-21-22).xlsx", "../data/sen-races/matt-dolan/matt-dolan-contributions-(4-21-22).xlsx", "../data/sen-races/morgan-harper/morgan-harper-contributions-(4-21-22).xlsx", "../data/sen-races/neil-patel/neil-patel-contributions-(4-21-22).xlsx", "../data/sen-races/tim-ryan/tim-ryan-contributions-(4-21-22).xlsx"])
    athens.run(["../data/treasurer-race/robert-sprague/robert-sprague-contributions-(4-21-22).xlsx", "../data/treasurer-race/scott-schertzer/scott-schertzer-contributions-(4-21-22).xlsx"])

    endTime = time.time()

    print(f"It took {endTime-startTime:.2f} seconds to generate these charts")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()