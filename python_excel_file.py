import requests
import xlrd
import xlwt
import sys
import json

inputPath = sys.argv[1]
inputColumn = sys.argv[2]


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
print(addresses)
data = {
    'addresses': json.dumps(addresses),
    'modelId':295,
    'projectId':186,
    'unmagnizedOnly': 'false'
}

# The authorization is a token get from LB Portal.
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3JfaWQiOjExODksInVzcl9uYW1lIjoiYm8uZ3VvQGdpc3RpY2luYy5jb20iLCJ1c3JfZW1haWwiOiJiby5ndW9AZ2lzdGljaW5jLmNvbSIsInVzcl9wcm9maWxlIjoie1wiQTNJXCI6e1wicm91dGVyU3RhdGVcIjpcImRpc2NvdmVyXCIsXCJ1cmxcIjpcIi9kaXNjb3ZlclwifX0iLCJ1c3Jfc3NvX25hbWUiOm51bGwsInVzcl9hZG1pbl9mbGFnIjp0cnVlLCJjdXNfbmFtZV9zaG9ydCI6IlRTU1ciLCJjdXNfaWQiOjEwMzMsInVzcl9zaWdudXBfc3RhdGUiOiJBQ1RJVkUiLCJwZXJtaXNzaW9ucyI6eyJBM0kiOnsidXNlclN1YnNjcmlwdGlvbklkIjozMX19LCJpYXQiOjE1NjA1MzE4NzQsImV4cCI6MTU5MjA2Nzg3NH0.QDpMvWC5UwMEVwtwUAMhAVYqN1cElnVidnyU7letOsc',
    'Accept-Encoding': 'gzip, deflate, br'
}

# Send request
r = requests.post(url, data = data, headers = headers)

# Clean result data
resultJson = json.loads(r.content)

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