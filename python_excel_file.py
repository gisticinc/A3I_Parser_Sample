import requests
import xlrd
import xlwt
import sys
import json

inputPath = sys.argv[1]
inputColumn = sys.argv[2]
inputToken = sys.argv[3]

try:
    inputPath
except:
    print("Please specify the source address file.")
    exit()

try:
    inputColumn
except:
    print("Please specify the address column name.")
    exit()

try:
    inputToken
except:
    print("Please provide the A3I token.")
    exit()


# Prepare addresses
# Get address column number
wb = xlrd.open_workbook(inputPath) 
sheet = wb.sheet_by_index(0)

for i in range(sheet.ncols): 
    if sheet.cell_value(0, i) == inputColumn:
        addressColumnNumber = i

# Load addresses
addresses = []
for j in range(1, sheet.nrows): 
    addresses.append(sheet.cell_value(j, addressColumnNumber))

# The endpoint of the service
url = 'https://api.linearbench.com/a3i/parse'

# Data to post:
# 1. Addresses to parse in an array
# 2. Project and Model to use. The default is a trained model.
# 3. Always set "unmagnizedOnly" to false
data = {
    'addresses': json.dumps(addresses),
    'modelId':295,
    'projectId':186,
    'unmagnizedOnly': 'false'
}

# The authorization is a token get from LB Portal.
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Authorization': inputToken,
    'Accept-Encoding': 'gzip, deflate, br'
}

# Send request
r = requests.post(url, data = data, headers = headers)

# Check error
if r.status_code != 200:
    print 'The parse process failed: ' + r.json()
    exit()

# Clean result data
resultJson = json.loads(r.content)
print r.status_code

# Create result sheet
wb2 = xlwt.Workbook()
ws2 = wb2.add_sheet('result')

# Write data
columnOrder = {}
for k in range(len(resultJson) - 1):
    if k == 0:
        column = 0
        for key in resultJson[k]:
            ws2.write(0, column, key)
            columnOrder[key] = column
            column = column + 1
    else:
        for key in resultJson[k]:
            if key in columnOrder:
                ws2.write(k, columnOrder[key], resultJson[k][key])
            else:
                ws2.write(0, column, key)
                columnOrder[key] = column
                ws2.write(k, column, resultJson[k][key])
                column = column + 1


# Save result
wb2.save('result.xls')