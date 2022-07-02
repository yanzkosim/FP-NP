# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests
import json

access_token = 'NWJhMmU5ODYtZDEyOS00NmFhLThkMDYtNmFjODkwODQxOTdjMzQ2MmRkYWMtNjM2_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54'
url = 'https://webexapis.com/v1/rooms'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))