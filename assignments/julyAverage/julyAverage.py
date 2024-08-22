import csv
import math

with open('julydata.txt', newline='') as csvfile:
    count=10
    flowreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    total = 0
    totalsq = 0
    count = 0
    for row in flowreader:
        if "USGS" in row :
            time=row[2]
            flow=int(row[4])
            total=total + flow
            toatlsq += flow*flow
            count+=1
#           print(time,', ',flow)
    mean=(total/count)
    variance=sqrt(toatlsq/count-mean*mean)
    print(count, ' ',mean,' ',variance)