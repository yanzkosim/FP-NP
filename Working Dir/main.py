import json
import requests

base_url = "http://localhost:58000/api/v1/"
username= "roxy"
password= "roxy"  


def get_ticket():
    headers = {"content-type": "application/json"}
    data = {"username": username, "password": password}

    response = requests.post(base_url+"ticket", headers=headers, json=data)
    ticket = response.json()
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

def get_network_device():
    headers={"X-Auth-Token": get_ticket()}
    resp = requests.get(base_url+"network-device", headers=headers, verify=False)
    print("Return code for Get Network Device: ", resp.status_code)

    response_json = resp.json()
    networkDevices = response_json["response"]

    for networkDevice in networkDevices:
        print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])

def get_host():
    headers={"X-Auth-Token": get_ticket()}
    resp = requests.get(base_url+"host", headers=headers, verify=False)
    print("Return code for Get Host: ", resp.status_code)

    response_json = resp.json()
    hosts = response_json["response"]

    for host in hosts:
        print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])

if __name__ == "__main__":
    print("Retrieving Network Devices...")
    get_network_device()
    print()
    print("Retrieving Hosts...")
    get_host()