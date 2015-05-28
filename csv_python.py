import csv
csvfile = open('elysee-csv.csv','r', encoding="utf8")

reader = csv.reader(csvfile, delimiter=',', quotechar='"')


RowCount = 0
for row in reader:
    RowCount += 1
    CellCount = 0
    if RowCount > 1:
        for cell in row:
            CellCount += 1
            if CellCount ==1:
                filename = cell + '.txt'
                f = open(filename, 'w', encoding="utf8")
            if CellCount == 3:
                f.write(cell)
                f.close()
