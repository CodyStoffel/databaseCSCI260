import csv

with open('julydata.txt', newline='') as csvfile:
    count=10
    flowreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for i in range(0,30):
        row = next(flowreader)
        print('], ['.join(row))