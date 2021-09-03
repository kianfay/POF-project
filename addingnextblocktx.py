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
    print(ret)
    if(i == 3):
        address = ret['result']

ret = instruct_wallet("generatetoaddress", [101, address])
firstBlockHash = ret['result'][0]
print(ret)

ret = instruct_wallet('getblock', [firstBlockHash])
txHex = ret['result']['tx'][0]
print(ret)

ret = instruct_wallet('createrawtransaction', [
    [{"txid":txHex, "vout":0}], 
    [{"data":"00010203"},{address:"0.01"}]
])
txHex = ret['result']
print(ret)

ret = instruct_wallet('signrawtransactionwithwallet', [txHex])
signedTx = ret['result']['hex']
print(ret)

ret = instruct_wallet('generateblock', [address, [signedTx]])
print(ret)