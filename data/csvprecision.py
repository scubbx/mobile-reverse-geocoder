""" This script reduces the coordinate precision of a CSV file containing
    WKT Polygons in the first row. """

import csv
#from shapely.wkb import dumps, loads

inputFile = 'lines_gen10+.csv'
outputFile = 'lines_gen10_4+.csv'
newData = []

with open(inputFile, 'r') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',',quotechar='"')
  spamreader.next()
  for row in spamreader:
    #print row[0]
    #oneline = loads(row[0])
    #print oneline
    editGeom = row[0][12:-1]
    newGeom = []
    for linePoint in editGeom.split(','):
      newPoint = ''
      linePointCoordinates = linePoint.split(' ')
      #print linePointCoordinates
      newPoint += str(round(float(linePointCoordinates[0]),4)) + ' '
      newPoint += str(round(float(linePointCoordinates[1]),4))
      newGeom.append(newPoint)
    
    newData.append(['LINESTRING ('+ ','.join(newGeom) +')',row[1]])
    #print newData

print "write..."

with open(outputFile, 'w') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=';',quotechar='"')
  spamwriter.writerow(['WKT','rasterval'])
  for row in newData:
    #print row
    spamwriter.writerow(row)
    
