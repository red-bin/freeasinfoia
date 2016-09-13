#!/usr/bin/python2.7

import requests
import json
import time
import sys

from pprint import pprint

response = requests.post(
  'https://www.muckrock.com/api_v1/token-auth/',
  data={
    'username': 'dischordic',
    'password': '1nf1n1nt' 
  }
)

token = response.json()['token']
title = 'Request for list of registerd FOIA/FOIL officers'
document = 'test123'

def get_response(url,page_no):
    headers = { 'Authorization': 'Token %s' % token }
    data = {'title':title,
            'document_request':document,
            'username': '',
            'password': '',
            'page_size':100,
            'page': page_no
     }

    response = requests.post(url, data=data)
    resp_json = json.loads(response.text)

    return response


stdin = sys.stdin.readlines()
start = stdin[0]
end = stdin[1]

for i in range(,6166):
    while True:
        try:
            url = 'https://www.muckrock.com/api_v1/agency'
            resp = get_response(url,i)
            print resp.text
            break
        except:
            time.sleep(5)
