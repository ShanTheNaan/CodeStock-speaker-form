import csv

filename = "flaskApp/upload/talkInfo.csv"

with open(filename, newline='') as csvfile:
  talks = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in talks: 
    print(', '.join(row))



