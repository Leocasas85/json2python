import json
import csv

sourceFile = open('/home/leo/Documents/GithubAPIjson/2_99_Brisbane.json', 'rU')

json_data =json.load(sourceFile)

print(json_data["items"])

outputFile = open('Githubconvertedjson.csv', 'w')

outputWriter = csv.writer(outputFile)

for items in json_data["items"]:
    row_array = []
    row_array.append(json_data["total_count"])
    for attribute in items:
       row_array.append(items[attribute])
    outputWriter.writerow(row_array)

sourceFile.close()
outputFile.close()

