import csv
import numpy

def cords_gen(measurement1, measurement2, dataset):
    cords = []
    with open (dataset) as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc1 = measurements.index(measurement1)
        loc2 = measurements.index(measurement2)
        for row in csvfile:
            temp = []
            temp.append(row[loc1])
            temp.append(row[loc2])
            cords.append(temp)
    
    return cords


def avg_and_sd_calc(inputlist):
    sd = numpy.std(inputlist)
    total = 0
    for item in inputlist:
        total += item
    avg = total/len(inputlist)
    return sd, avg