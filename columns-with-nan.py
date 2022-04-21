import pandas

AMOUNT = 17

def main():
    df = pandas.read_excel("SPREADSHEETS\DATE FOUND_ 3-31-22\GOV RACES\contributions\(SOS) BLYSTONE CONTRIB - 1_31_22 .xlsx", header = 1)
    columns = df.values.T.tolist()

    for i in range(len(columns[AMOUNT])):
        if pandas.isna(columns[AMOUNT][i]):
            print(f"Row {i + 3} doesn't have a number in column AMOUNT")
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()