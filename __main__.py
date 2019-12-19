# from numpy import *
import re
import json
import csv
from simple_chalk import chalk
from datetime import datetime


# Clean single row


def cleanRow(row):
    cleanRow_01 = re.sub('\s\s+', ' ', row)
    cleanRow_02 = re.sub('\º', '', cleanRow_01)
    cleanRow_03 = re.sub('\,', '.', cleanRow_02)
    cleanRow_array = cleanRow_03.split(' ')

    for i, cell in enumerate(cleanRow_array):
        cleanRow_array[i] = float(cell)

    return cleanRow_array


#
# Get dataset
datasetBuffer = open('data/raw/dataset.txt', 'r')
dataset = datasetBuffer.read()
datasetBuffer.close()
print(chalk.green('dataset getted from \'data/raw/dataset.txt\''))

#
# Get header
header = dataset.split('\n')[0]
headerSafe = re.split('\s', header)
headerSafe = list(filter(lambda h: h, headerSafe))

#
# Get rows
rows = dataset.split('\n')[1:]
rowsSafe = []
for row in rows:
    rowsSafe.append(cleanRow(row))  # from cleanRow()

#
# Clean whole data
dataSafe = []
dataSafe.append(headerSafe)
for r in rowsSafe:
    dataSafe.append(r)

#
# ToJSON
dataJSON = []
for i, dataRow in enumerate(dataSafe[1:]):
    obj = {
        "id": i,
        "geom": {
            "long": dataRow[0],
            "lat": dataRow[1]
        },
        "temperatures": dataRow[2:-1]
    }
    dataJSON.append(obj)


#
# Load in file
now = datetime.now().strftime('%Y%m%d_%H%M%S')
f = open(f'data/processed/{now}.json', "x")
f.write(json.dumps(dataJSON))
f.close()
print(chalk.green(f'dataset setted as JSON in \'data/processed/{now}.json\''))


#
# To CSV
with open(f'data/processed/{now}.csv', "x") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(map(lambda h: h.lower(), headerSafe[:-1]))
    for r in rowsSafe:
        csv_writer.writerow(r[:-1])
print(chalk.green(f'dataset setted as CSV in \'data/processed/{now}.csv\''))


#
# ToPostGres


print(chalk.green('data processed into \'data/processed/\''))
print(chalk.bgGreen.bold('exit code 0'))
