import requests

inputToken = sys.argv[1]

try:
    inputToken
except:
    print("Please provide the A3I token.")
    exit()

# The endpoint of the service
url = 'https://api.linearbench.com/a3i/parse'

# Data to post:
# 1. Addresses to parse in an array
# 2. Project and Model to use. The default is a trained model.
# 3. Always set "unmagnizedOnly" to false
data = {
    'addresses':'["4380 FAIRWAY DRIVE LAKE MONTEZUMA 86342","8 ACR 3160 VERNON 85940","889 ACR 3144 VERNON 85940","ACR 3137 LOT 24 VERNON 85940","ACR 3142 LOT 842 VERNON 85940","ACR 3176 HOUSE 4 VERNON 85940","ACR 3324 LOT 79 VERNON 85940","APN 106-64-006 VERNON 85940"]',
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

# Print the response
print r.content