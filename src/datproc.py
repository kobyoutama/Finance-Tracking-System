# datproc.py: Class to take in lines and output a CSV or
#   updated CSV
# FTS Headers :
#   Description
#   Cost

import re
import csv
import helpers
from exceptions import InvalidDimensionError, InvalidWritePath
from os import getcwd, remove
from os.path import exists


class DataProc:
    HEADER = ["Date", "Description", "Cost"]
    FILE_PATH = getcwd() + '/../Out/fts_dat.csv'
    REGULAR_EXPRESSION = r"^fts_dat(\(\d?\d?\))?.csv$"

    def __init__(self, file=FILE_PATH) -> None:
        self.file = helpers.parsefile(file)
        self.header = DataProc.HEADER
        self.data = []

    # noinspection PyDefaultArgument
    def createCSV(self, header=HEADER, data=None):
        self.header = header
        self.data = data
        if not exists(self.file):
            with open(self.file, 'w+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
                if isinstance(self.data, list):
                    self.writeRows(self.data)
        else:
            self.file = helpers.newFile(self.file)
            with open(self.file, 'w+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
                if isinstance(self.data, list):
                    self.writeRows(self.data)

    def changeCSV(self, file) -> None:
        new_file = helpers.parsefile(file)
        if exists(new_file):
            self.file = new_file
        else:
            raise InvalidWritePath("File does not exist")

    def writeRow(self, row: []) -> None:
        if len(row) != len(self.header)-1:
            raise InvalidDimensionError(f"Row Dimension of {len(row)} != Header Dimension of {len(self.header)}")
        if exists(self.file):
            with open(self.file, 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([helpers.gettime()]+row)
        else:
            raise InvalidWritePath(f"file {self.file} does not exist to write")

    def writeRows(self, rows: [[]]) -> None:
        for row in rows:
            self.writeRow(row)

    def delRow(self, row: int) -> None:
        with open(self.file, 'r') as rf:
            lines = csv.reader(rf)
            lines = [line for line in lines]
        if row >= len(lines): raise IndexError(f"Row of {row} is out of bounds")
        with open(self.file, 'w', encoding='UTF8', newline='') as wf:
            for c, line in enumerate(lines):
                if c != row:
                    writer = csv.writer(wf)
                    writer.writerow(line)

    def editCSV(self, row: int, col: int, edit: str):
        if col >= len(self.header): raise IndexError(f"Column of {col} is out of bounds")
        with open(self.file, 'r') as rf:
            lines = csv.reader(rf)
            lines = [line for line in lines]
        if row >= len(lines): raise IndexError(f"Row of {row} is out of bounds")
        with open(self.file, 'w', encoding='UTF8', newline='') as wf:
            for i, line in enumerate(lines):
                if i == row:
                    line[col] = edit
                writer = csv.writer(wf)
                writer.writerow(line)

    def readCSV(self, print_header=False) -> str:
        with open(self.file, 'r') as rf:
            lines = csv.reader(rf)
            data = []
            if not print_header: next(lines)
            for line in lines:
                data.append(line)
                print('\t'.join(line))
        return data

    def readRow(self, row) -> str:
        with open(self.file, 'r') as rf:
            lines = csv.reader(rf)
            for i, line in enumerate(lines):
                if i == row:
                    print('\t'.join(line))
                    return line

    def readCol(self, col):
        if col >= len(self.header): raise IndexError(f"Column of {col} is out of bounds")
        with open(self.file, 'r') as rf:
            lines = csv.reader(rf)
            col_array = []
            header = next(lines)
            print(f'Column: {header[col]}')
            for line in lines:
                if len(line) < col:
                    col_array.append(None)
                    print(None)
                else:
                    col_array.append(line[col])
                    print(line[col])
        return col_array

    @staticmethod
    def delCSV(path: str) -> bool:
        path = path if path.startswith(f"{getcwd()}/../Out") else f"{getcwd()}/../Out/{path}"
        if path.endswith('.csv') and exists(path):
            remove(path)
            return True
        else:
            return False

if __name__ == "__main__":
    # ctr + / to chunk comment

    from os import listdir
    print("DatProc")
    DataProc.delCSV('fts_dat.csv')
    s = DataProc()
    s.createCSV()
    s.writeRows([['Chicken',20],['Beef', 10],["Asparagus", 15]])
    s.readCSV(True)
    print(s.readCol(1))
    s.editCSV(1,2,'5')
    s.editCSV(1,3,2)
    # s.readCSV(True)
    # s.readRow(1)
    # s.delRow(2)
    # for x in listdir(getcwd()+'/../Out'):
    #     print(DataProc.delCSV(DataProc, f'{getcwd()}/../Out/{x}'))
    #     DataProc.delCSV(DataProc,x)
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



