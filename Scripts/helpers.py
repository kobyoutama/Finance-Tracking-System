from time import time, strftime, localtime

def getTime() -> ('Day', 'Month', 'Year'):
    curr = time()
    t = strftime("%d %b %Y", localtime(curr))
    return t