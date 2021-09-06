#!/usr/bin/env python

import json
import requests    

""""""""""""
"""
Makes a bitcoin-cli request using the RPC service

Parameters:
    - method    - the bitcoin-cli method to use
    - params    - the parameters to pass, in an array
"""
""""""""""""
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



""""""""""""
"""
Adds proof of flow transactions to a block

Parameters:
    - blocksWithCoinbase    - an array of blocks from which to take the coinbase to make a new tx
    - address               - the address to send the new coinbase to
    - customData            - the gen string or for non-first txs, the hash of the previous txs
"""
""""""""""""
def addCustomTxsAndReadIt(blocksWithCoinbase, address, customData):
    
    signedTxs = []
    for block in blocksWithCoinbase:
        method = 'getblock';
        ret = instruct_wallet(method, [block])
        txHex = ret['result']['tx'][0]
        print(str(method),':\n', ret,'\n')

        method = 'createrawtransaction';
        ret = instruct_wallet(method, [
            [{"txid":txHex, "vout":0}], 
            [{"data":customData},{address:"0.01"}]
        ])
        txHex = ret['result']
        print(str(method),':\n', ret,'\n')

        method = 'signrawtransactionwithwallet';
        ret = instruct_wallet(method, [txHex])
        signedTxs.append(ret['result']['hex'])
        print(str(method),':\n', ret,'\n')

    method = 'generateblock'
    ret = instruct_wallet(method, [address, signedTxs])
    newBlockAddr = ret['result']['hash']
    print(method,':\n', ret,'\n')

    method = 'getblock'
    ret = instruct_wallet(method, [newBlockAddr])
    newTxHex = ret['result']['tx'][1]
    print(method,':\n', ret,'\n')

    method = 'getrawtransaction'
    ret = instruct_wallet(method, [newTxHex, True, newBlockAddr])
    txHex = ret['result']
    print(method,':\n', ret,'\n')

    return signedTxs
