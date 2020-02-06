import requests

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
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3JfaWQiOjExODksInVzcl9uYW1lIjoiYm8uZ3VvQGdpc3RpY2luYy5jb20iLCJ1c3JfZW1haWwiOiJiby5ndW9AZ2lzdGljaW5jLmNvbSIsInVzcl9wcm9maWxlIjoie1wiQTNJXCI6e1wicm91dGVyU3RhdGVcIjpcImRpc2NvdmVyXCIsXCJ1cmxcIjpcIi9kaXNjb3ZlclwifX0iLCJ1c3Jfc3NvX25hbWUiOm51bGwsInVzcl9hZG1pbl9mbGFnIjp0cnVlLCJjdXNfbmFtZV9zaG9ydCI6IlRTU1ciLCJjdXNfaWQiOjEwMzMsInVzcl9zaWdudXBfc3RhdGUiOiJBQ1RJVkUiLCJwZXJtaXNzaW9ucyI6eyJBM0kiOnsidXNlclN1YnNjcmlwdGlvbklkIjozMX19LCJpYXQiOjE1NjA1MzE4NzQsImV4cCI6MTU5MjA2Nzg3NH0.QDpMvWC5UwMEVwtwUAMhAVYqN1cElnVidnyU7letOsc',
    'Accept-Encoding': 'gzip, deflate, br'
}

# Send request
r = requests.post(url, data = data, headers = headers)

# Print the response
print r.content