# program originally created by Raphaël Hubain, rhubain@ulb.ac.be
import csv
csvfile = open('filename.csv','r', encoding="utf8") # replace "filename.csv" by the name of your file

reader = csv.reader(csvfile, delimiter=',', quotechar='"') # we're asking python to read the csv and to store the info in the variable reader


RowCount = 0  
for row in reader:        # simple counting procedure to go through the csv
    RowCount += 1
    CellCount = 0
    if RowCount > 1:     
        for cell in row:
            CellCount += 1
            if CellCount ==1:  # if we're in the row number one, we take the content and use it as the filename for a new text file
                filename = cell[:50] + '.txt' # let's limit filename to 50 chars
                f = open(filename, 'w', encoding="utf8")
            if CellCount == 3: # if we're in the row number three, we take the content and use it as the content of the previoulsy created file
                f.write(cell)
                f.close()
