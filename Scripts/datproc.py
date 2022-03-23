# datproc.py: Class to take in lines and output a CSV or
#   updated CSV
# FTS Headers :
#   Description
#   Cost

import csv
import helpers
from os import remove as file_remove
from os.path import exists as file_exists


class NotImplementedError(Exception):
    pass

class InvalidDimensionError(Exception):
    pass

class InvalidWritePath(Exception):
    pass

class DataProc():
    HEADER = ["Date", "Description", "Cost"]
    FILE_PATH = '../Out/fts_dat.csv'
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
            raise NotImplementedError("createCSV path not implemented")

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


if __name__ == "__main__":
    print("DatProc")
    s = DataProc()
    # ctr + / to chunk comment
    s = DataProc()
    s.delCSV(s.FILE_PATH)
    s.createCSV()
    s.writeRow(['Test','',123])
    s.writeRow(['test',None,321])
    s.writeRow(['yes',2,1])
