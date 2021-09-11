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
    url = 'http://127.0.0.1:18443/'
    payload = json.dumps({'jsonrpc': '1.0', 'id': 'curltest', 'method': method, 'params': params})
    headers = {'content-type': 'text/plain'}
    try:
        response = requests.request('POST', url, data=payload, headers=headers, auth=('USERNAME', 'PASSWORD'))
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
        print(str(method),':\n', ret,'\n')
        txHex = ret['result']['tx'][0]

        method = 'createrawtransaction';
        ret = instruct_wallet(method, [
            [{"txid":txHex, "vout":0}], 
            [{"data":customData},{address:"0.01"}]
        ])
        print(str(method),':\n', ret,'\n')
        txHex = ret['result']
        

        method = 'signrawtransactionwithwallet';
        ret = instruct_wallet(method, [txHex])
        print(str(method),':\n', ret,'\n')
        signedTxs.append(ret['result']['hex'])

    method = 'generateblock'
    ret = instruct_wallet(method, [address, signedTxs])
    print(method,':\n', ret,'\n')
    newBlockAddr = ret['result']['hash']

    method = 'getblock'
    ret = instruct_wallet(method, [newBlockAddr])
    print(method,':\n', ret,'\n')
    newTxHex = ret['result']['tx'][1]

    method = 'getrawtransaction'
    ret = instruct_wallet(method, [newTxHex, True, newBlockAddr])
    print(method,':\n', ret,'\n')
    txHex = ret['result']

    return signedTxs

""""""""""""
"""
Returns the noncoinbase txs with the blockhash of the containing block
e.g. {"txids": ["txid1", "txid2"], "blockhash": "hash"}

Parameters:
    - blockHeight
"""
""""""""""""
def returnNonCoinbaseTxs(blockHeight):
    method = 'getblockhash'
    ret = instruct_wallet(method, [blockHeight])
    print(method,':\n', ret,'\n')
    blockHash = ret['result']

    if(ret['error'] != None):
        print('Height passed to the function returnNonCoinbaseTxs is out of range...')
        return

    method = 'getblock'
    ret = instruct_wallet(method, [blockHash])
    print(method,':\n', ret,'\n')
    returnedTxs = ret['result']['tx']

    if len(returnedTxs) < 2:
        print('This block only has a coinbase tx')
        return False
    
    returnedTxs = returnedTxs[1:]
    return  {
                'txids': returnedTxs, 
                'blockhash': blockHash
            }



def getHeightOfBlockchain():
    method = 'getbestblockhash'
    ret = instruct_wallet(method, [])
    print(method,':\n', ret,'\n')
    bestBlockHash = ret['result']

    method = 'getblock'
    ret = instruct_wallet(method, [bestBlockHash])
    print(method,':\n', ret,'\n')
    heightOfBestBlock = ret['result']['height']
    
    return heightOfBestBlock

