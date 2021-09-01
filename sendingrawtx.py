#!/usr/bin/env python

import json
import requests    

def instruct_wallet(method, params):
    url = "http://127.0.0.1:18443/"
    payload = json.dumps({"jsonrpc": "1.0", "id": "curltest", "method": method, "params": params})
    headers = {'content-type': "text/plain"}
    try:
        response = requests.request("POST", url, data=payload, headers=headers, auth=("USERNAME", "PASSWORD"))
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(e)
    except:
        print('No response from Wallet, check Bitcoin is running on this machine')

""" answer = instruct_wallet("getblockhash", [2])
print(answer) """
