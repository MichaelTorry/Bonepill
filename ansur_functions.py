import csv
import numpy as numpy

def cordsgen(measurement1, measurement2):
    malecords = []
    with open ("ansur-female.csv") as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc1 = measurements.index(measurement1)
        loc2 = measurements.index(measurement2)
        for row in csvfile:
            temp = []
            temp.append(row[loc1])
            temp.append(row[loc2])
            malecords.append(temp)
    femalecords = []
    with open ("ansur-female.csv") as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc1 = measurements.index(measurement1)
        loc2 = measurements.index(measurement2)
        for row in csvfile:
            temp = []
            temp.append(row[loc1])
            temp.append(row[loc2])
            femalecords.append(temp)
    cords = []
    cords.append(femalecords)
    cords.append(malecords)

    return cords


def SDcalc(inputlist):
    return numpy.std(inputlist)