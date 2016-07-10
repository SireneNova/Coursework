import os, csv

# The path to the script
currentPath = os.path.dirname(os.path.abspath('__file__'))
#quotation marks around file diff in mac

# Make the spreadsheet path
outputCsv = currentPath + '\spreadsheet.csv'
print outputCsv

# Open the file
csvFile = open(outputCsv, 'wb')

# Create writer object
writer = csv.writer(csvFile, delimiter=',')

# Data to go in csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

'''
# Write rows to csv
writer.writerow(row_1)
writer.writerow(row_2)
writer.writerow(row_3)

or instead loop, below:
'''
#need to close the python shell to see changes

# All rows
rows = [row_1, row_2, row_3]

# Loop rows and write each
for row in rows:
    writer.writerow(row)
