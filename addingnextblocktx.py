from bitcoinCliUtil import instruct_wallet
from bitcoinCliUtil import addCustomTxsAndReadIt
import hashlib
import json

""""""""""""""""""
""""""""""""
"""
Putting a hash of 2 txs in block X, into the new tx in block X+1.

First we crete and load a wallet.
"""
""""""""""""
""""""""""""""""""

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

""""""
""" 
Generate enough blocks for Y coinbase txs to make raw txs from.
Y=3
"""
""""""

method = 'generatetoaddress'
ret = instruct_wallet(method, [103, address])
blockHashes = ret['result']
print(str(method),':\n', ret,'\n')

""" "gen".toAscii() = 67656e """
signedTxs = addCustomTxsAndReadIt([blockHashes[0], blockHashes[1]] , address, "67656e")


""""""
""" 
Adding the hash from the genesis tx to the next tx.
Using secondBlockHash now  to get a new coinbase tx.
"""
""""""

print('\n\n', 'Plain txs: ', str(signedTxs), '\n')
hashedTx = hashlib.sha256(bytes(str(signedTxs), 'utf-8')).hexdigest()
print('\n\n', 'Hashed txs: ', hashedTx, '\n')

signedTx = addCustomTxsAndReadIt([blockHashes[2]], address, hashedTx)