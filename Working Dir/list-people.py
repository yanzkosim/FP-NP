# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'NWJhMmU5ODYtZDEyOS00NmFhLThkMDYtNmFjODkwODQxOTdjMzQ2MmRkYWMtNjM2_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zOGZjMDc3Zi1kMTQwLTRjZGEtYTAzZC01ZTdkNzQzYjY2MjI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
# params = {
#     'email': 'kosim957@gmail.com'
# }
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))