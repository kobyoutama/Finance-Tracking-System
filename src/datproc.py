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
from os import getcwd, listdir, remove
from os.path import exists, splitext


class DataProc:
    HEADER = ["Date", "Description", "Cost"]
    FILE_PATH = getcwd() + '/../Out/fts_dat.csv'
    REGULAR_EXPRESSION = r"^fts_dat(\(\d?\d?\))?.csv$"

    def __init__(self, file=FILE_PATH, header=HEADER) -> None:
        self.file = helpers.parsefile(file)
        self.header = header

    def createCSV(self):
        if not exists(self.file):
            with open(self.file, 'w+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
        else:
            self.file = helpers.newFile(self.file)
            with open(self.file, 'w+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)

    def writeRow(self, row: []) -> int:
        if len(row) != len(self.header):
            raise InvalidDimensionError(f"Row Dimension of {len(row)} != Header Dimension of {len(self.header)}")
        if exists(self.file) :
            with open(self.file, 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([helpers.getTime()]+row)
            return 1
        else:
            raise InvalidWritePath("No working CSV file")

    def delCSV(self, path: str) -> int:
        path = path if path.startswith(f"{getcwd()}/../Out") else f"{getcwd()}/../Out/{path}"
        if path.endswith('.csv') and exists(path):
            remove(path)
            return 1
        else:
            return 0

    def delRow(self, desc, val) -> int:
        raise NotImplementedError("delRow not implemented")

    def editCSV(self, row: int, col: int, file):
        if not exists(file):
            raise InvalidWritePath("No working CSV file")
        raise NotImplementedError("Edit CSV not implemented")


if __name__ == "__main__":
    # ctr + / to chunk comment
    print("DatProc")
    # for x in listdir(getcwd()+'/../Out'):
    #    print(DataProc.delCSV(DataProc, f'{getcwd()}/../Out/{x}'))
    #    DataProc.delCSV(DataProc,x)
    #
    # s = DataProc("asd.csv")
    # s.createCSV()
    # s = DataProc("das")
    # s.createCSV()
    # s = DataProc(getcwd()+"/../Out/sad.csv")
    # s.createCSV()
    # s = DataProc("asd.csv")
    # s.createCSV()
    # s = DataProc()
    # s.createCSV()
