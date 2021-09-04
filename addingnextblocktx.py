from bitcoinCliUtil import instruct_wallet
from bitcoinCliUtil import addCustomTxAndReadIt
import hashlib
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

method = 'generatetoaddress'
ret = instruct_wallet(method, [102, address])
firstBlockHash = ret['result'][0]
secondBlockHash = ret['result'][1]
print(str(method),':\n', ret,'\n')

""" "gen".toAscii() = 67656e """
signedTx = addCustomTxAndReadIt(firstBlockHash, address, "67656e")


""""""
""" 
Adding the hash from the genesis tx to the next tx.
Using secondBlockHash now  to get a new coinbase tx.
"""
""""""

hashedTx = hashlib.sha256(bytes(signedTx, 'utf-8')).hexdigest()
print('\n\n', 'Hashed tx: ', hashedTx, '\n')

signedTx = addCustomTxAndReadIt(secondBlockHash, address, hashedTx)