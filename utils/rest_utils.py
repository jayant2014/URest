import requests, json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Standalone script to check api requests, modify your url, port, endpoints to get requests

base_url = 'abc.com'
base_port = '1234'
base_version = v1
token = None
test_cert = 'my_agent.cert'
test_key = 'my_agent.key'
test_ica = 'my_agent.cacert'

def get_headers():
    token = 'abcd'
    header_list = {
        'Authorization': "Bearer " + token,
        'Content-type': "application/json"
    }
    return header_list

def get_requests(endpoint):
    header_list = get_headers()
    url = 'https://' + base_url + ':' + base_port + '/' + base_version + '/' + endpoint
    resp = requests.get(url, cert=(test_cert,test_key), headers=header_list, verify=False)
    resp_list = json.loads(resp.text)
    return resp_list, resp.status_code

def post_requests(payload_json, endpoint):
    header_list = get_headers()
    with open(payload_json, 'rb') as payload:
        url = 'https://' + base_url + ':' + base_port + '/' + base_version + '/' + endpoint
        resp = requests.post(url, data=payload, cert=(test_cert,test_key),headers=header_list, verify=False)
        resp_list = json.loads(resp.text)

    return resp_list

def post_requests_verify(payload_json, endpoint):
    header_list = get_headers()
    resp = requests.post(url, data=json.dumps(payload_json), headers=header_list, verify=test_ica)


msg = dict()
(resp_list, status_code) = get_requests('myfiles')
msg["key"] = json.loads(resp_list.text)["key"]
get_data = 'https://' + base_url + ':' + base_port + '/' + base_version + '/' + msg['key']
data = json.loads(get_data.text)
print(data)

resp_list = post_requests('data.json', addfiles)
data = json.loads(resp_list.text)
print(data)

# invalid format get_url = 'https://' + base_url + ':' + base_port + '/' + base_version + '/' + invalidendpoint
