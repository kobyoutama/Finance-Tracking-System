# datproc.py: Class to take in lines and output a CSV or
#   updated CSV
# FTS Headers :
#   Description
#   Cost

import re
import csv
import helpers
import pandas as pd
from exceptions import NotImplementedError, InvalidDimensionError, InvalidWritePath
from os import getcwd, listdir
from os import remove as file_remove
from os.path import exists as file_exists


class DataProc():
    HEADER = ["Date", "Description", "Cost"]
    FILE_PATH =  getcwd() + '/../Out/fts_dat.csv'
    REGULAR_EXPRESSION = r"^fts_dat(\(\d\))?.csv$"

    def __init__(self) -> None:
        pass

    def createCSV(self, file=FILE_PATH, header=HEADER):
        self.file = file
        self.header = header
        if not file_exists(self.file):
            with open(self.file, 'w+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
        else:
            # this path will create a new file with new added or subtracted headers
            # self.file = self.file[:-3] + '(%d)'.format(len[]) + .csv
            cf = len([f for f in listdir(path='../Out') if re.match(DataProc.REGULAR_EXPRESSION,f)])
            self.file = getcwd() + f'/../Out/fts_dat({cf}).csv'
            with open(self.file, 'w+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
            # cf = len([f for f in listdir(path='../Out') if f.startswith('') and f.endswith('.csv')])

    def writeRow(self, row: []) -> int:
        if len(row) != len(self.header):
            raise InvalidDimensionError(f"Row Dimension of {len(row)} != Header Dimension of {len(self.header)}")
        if file_exists(self.file) :
            with open(self.file, 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([helpers.getTime()]+row)
            return 1
        else:
            raise InvalidWritePath("No working CSV file")

    def delCSV(self, path: str) -> int:
        if path.endswith('.csv') and file_exists(path):
            file_remove(path)
            return 1
        else:
            return 0

    def delRow(self, desc, val) -> int:
        raise NotImplementedError("delRow not implemented")

    def editCSV(self, row: int, col: int, file):
        if not file_exists(file):
            raise InvalidWritePath("No working CSV file")
        raise NotImplementedError("Edit CSV not implemented")

if __name__ == "__main__":
    print("DatProc")
    s = DataProc()
    # ctr + / to chunk comment
    s = DataProc()
    s.delCSV(getcwd()+f"/../Out/fts_dat(10).csv")
