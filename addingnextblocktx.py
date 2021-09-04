from sendingrawtx import instruct_wallet
import json


methodAndParams = [
    ['createwallet', 
        ['regtest']
    ],
    ['loadwallet', 
        ['regtest']
    ],
    ['getblockhash', 
        [0]
    ],
    ['getnewaddress', 
        []
    ]
]

address = None;
for i in range(0,4):
    ret = instruct_wallet(methodAndParams[i][0], methodAndParams[i][1])
    print(ret,'\n')
    if(i == 3):
        address = ret['result']

method = 'generatetoaddress';
ret = instruct_wallet(method, [101, address])
firstBlockHash = ret['result'][0]
print(str(method),':\n', ret,'\n')

method = 'getblock';
ret = instruct_wallet(method, [firstBlockHash])
txHex = ret['result']['tx'][0]
print(str(method),':\n', ret,'\n')

method = 'createrawtransaction';
ret = instruct_wallet(method, [
    [{"txid":txHex, "vout":0}], 
    [{"data":"00010203"},{address:"0.01"}]
])
txHex = ret['result']
print(str(method),':\n', ret,'\n')

method = 'signrawtransactionwithwallet';
ret = instruct_wallet(method, [txHex])
signedTx = ret['result']['hex']
print(str(method),':\n', ret,'\n')

method = 'generateblock'
ret = instruct_wallet(method, [address, [signedTx]])
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