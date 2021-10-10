import csv
import json

def csv_to_json(csvFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    jsonString = json.dumps(jsonArray, indent=4)
    print(jsonString)


csv_to_json(r'TestData.csv')

