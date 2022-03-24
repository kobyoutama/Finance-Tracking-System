import os.path
from time import time, strftime, localtime
from os import getcwd
from os.path import splitext, exists

def gettime() -> str("year-month-date"):
    curr = time()
    t = localtime(curr)
    return "-".join([str(t[0]), str(t[1]), str(t[2])])

def parsefile(f:str) -> str:
    cwd = getcwd() + '/../Out/'
    if f.endswith('.csv'):
        if f.startswith(cwd):
            return f
        return f"{cwd}{f}"
    elif f.startswith(cwd):
        return f'{f}.csv'
    else:
        return f'{cwd}{f}.csv'

def newFile(f:str) -> str:
    name,ext = splitext(f)
    fnew = f
    i = 0
    while exists(fnew):
        i += 1
        fnew = f'{name}({i}){ext}'
    return parsefile(fnew)

if __name__ == '__main__':
    print(getTime())