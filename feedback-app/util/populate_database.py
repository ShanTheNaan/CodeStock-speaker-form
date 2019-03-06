import csv

filename = "../upload/talkInfo.csv"

with open(filename, newline='') as csvfile:
  talks = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in talks: 
    print(row)
    print(', '.join(row))



