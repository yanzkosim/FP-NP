# Fill in this file with the messages code from the Webex Teams exercise
# Fill in this file with the membership code from the Webex Teams exercise
import requests
import json

access_token = 'NWJhMmU5ODYtZDEyOS00NmFhLThkMDYtNmFjODkwODQxOTdjMzQ2MmRkYWMtNjM2_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOTBjMzY0YTAtZjZlOS0xMWVjLTgxMjYtZWJmM2RkNDVjNzBk'
message = 'Halo Roxy'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())