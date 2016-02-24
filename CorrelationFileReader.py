__author__ = 'Matthew'

import os
import sys

dir = os.path.dirname(__file__)
DATA = os.path.join(dir, 'data.txt')
LOGS = os.path.join(dir, 'results/')

class Finder:

    def __init__(self):

        self.X = []
        self.Y = []
        self.XY = {}
        self.YX = {}
        self.points = {}
        print("starting...")
        with open(DATA, 'r') as f:
            for rawRow in f:
                row = rawRow.strip()
                if "|||" in row:
                    xVal = row.split("|||")[1].replace(":", "")
                    self.X.append(xVal)
                    self.XY[xVal] = {}
                elif "||" in row:
                    rawSplit = row.split("||, ")
                    XYSplit = rawSplit[0].split(" -> ")
                    xVal = XYSplit[0]
                    yVal = XYSplit[1]
                    val = rawSplit[1]
                    try:
                        _ = self.XY[xVal][yVal]
                        self.XY[xVal][yVal] = val
                        self.YX[yVal][xVal] = val
                    except:
                        self.Y.append(yVal)
                        self.YX[yVal] = {xVal : val}
                        self.XY[xVal][yVal] = val


    def buildX(self, ls):
        self.X = ls[1:]
        for item in ls[1:]:
            self.XY[item] = {}

    def queryOne(self, z):
        if(z in self.X):
            return self.XY[z]
        elif(z in self.Y):
            return self.YX[z]
        else:
            return {}

    def queryTwo(self, x, y):
        if(x in self.X and y in self.Y):
            return self.XY[x][y]
        elif(x in self.Y and y in self.X):
            return self.YX[x][y]
        else:
            return ""

def sort(dict):
    new = []
    for k in dict:

        if new == []:
            new.append([k, dict[k]])
        else:
            placed = False
            for i in range(0, len(new)):
                if float(new[i][1]) < float(dict[k]):
                    new = new[:i] + [[k, dict[k]]] + new[i:]
                    placed = True
                    break
                elif float(new[i][1]) > float(dict[k]):
                    pass
            if placed == False:
                new.append([k, dict[k]])
    return new

def writelog(logName, logString):
    f = open(LOGS + logName, "w")
    f.write(logString)
    f.close()

def submitQuery(finder, items):
    logString = ""
    logName = ""
    args = raw_input("Please submit a query (x&y or x): ").split("&")
    if len(args) == 1:
        logName = args[0] + ".txt"
        res = finder.queryOne(args[0])
        sorted = sort(res)
        if sorted == []:
            print({})
        else:
            count = 0
            for pair in sorted:
                if count <= items:
                    print(pair[0] + " -> " + pair[1])
                logString += pair[0] + " -> " + pair[1] + "\n"
                count += 1
        if logString != "":
            writelog(logName, logString)
    elif len(args) == 2:
        res = finder.queryTwo(args[0], args[1])
        logString = res
        logName = args[0] + "&" + args[1] + ".txt"
        print(res)
        if logString != "":
            writelog(logName, logString)
    else:
        print("Argument Error")


if __name__ == "__main__":
    print("starting...")
    finder = Finder()
    items = int(raw_input("How many entries should be displayed? "))
    running = True
    submitQuery(finder, items)
    while running == True:
        response = raw_input("Another query? y or n ")
        if response == "y":
            submitQuery(finder, items)
        elif response == "n":
            running = False
            break
        else:
            print("Response error")