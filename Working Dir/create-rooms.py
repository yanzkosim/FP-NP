# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests
import json

access_token = 'NWJhMmU5ODYtZDEyOS00NmFhLThkMDYtNmFjODkwODQxOTdjMzQ2MmRkYWMtNjM2_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54'
url = 'https://webexapis.com/v1/rooms'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'title': 'Ruangan Berkemah'}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))

id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOTBjMzY0YTAtZjZlOS0xMWVjLTgxMjYtZWJmM2RkNDVjNzBk'