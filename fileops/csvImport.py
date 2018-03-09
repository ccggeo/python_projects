import csv

with open('/Users/cgeorge/Documents/Book2.csv') as csvfile:
    readCSV = csv.reader(csvfile, dialect=csv.excel_tab)
    row1 =[]
   
   
    for row in readCSV:
        r = row[0]
        row1.append(r)


print(row1)
