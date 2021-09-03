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
    ],
    ['generatetoaddress', 
        [1]
    ],
    ['generateblock', 
        []
    ],
    ['createrawtransaction', 
        [
            [{"txid":"bf0a1ff2bd50bc02d391c25ccd3cba7458032ddbf45a9ced1375d2b9e5b82bfa", "vout":0}], 
            [{"data":"00010203"},{"bcrt1q0n6gls7nt336nu2y7negu3fy9c2qqkfd560eh7":"1"}]
        ]
    ],
    ['signrawtransactionwithwallet', 
        []
    ]
]

address = None;
for i in range(0,4):
    ret = instruct_wallet(methodAndParams[i][0], methodAndParams[i][1])
    print(ret)
    if(i == 3):
        address = ret['result']

methodAndParams[4][1].append(address)
ret = instruct_wallet(methodAndParams[4][0], methodAndParams[4][1])
print(ret)

methodAndParams[5][1].append(address)
methodAndParams[5][1].append([])
ret = instruct_wallet(methodAndParams[5][0], methodAndParams[5][1])
print(ret)


""" rawtx = instruct_wallet(methodAndParams[0][0], methodAndParams[0][1])
print(rawtx)

loadressult = instruct_wallet(methodAndParams[1][0], methodAndParams[1][1])
print(loadressult)

loadressult = instruct_wallet(methodAndParams[2][0], methodAndParams[2][1])
print(loadressult)

signedtx = instruct_wallet(methodAndParams[3][0], [rawtx['result']])
print(signedtx) """