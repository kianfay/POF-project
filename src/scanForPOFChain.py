from bitcoinCliUtil import instruct_wallet
from bitcoinCliUtil import returnNonCoinbaseTxs 
from bitcoinCliUtil import getHeightOfBlockchain
import hashlib

GENESIS_STRING = "67656e"

""""""""""""
"""
Scans the blockchain from a given start block which needs to contain the
genesis tx. Returns the number of txs in the POF chain in the main
blockchain in the same format as the punchcard passed to runCustomChain() 

Parameters:
    - startBlock    - the genesis tx's block 
"""
""""""""""""
def scanChain(startBlock):
    """"""
    """
    Get the height of the blockchain and scan the block at the height - startBlock

    Extract the raw gen txs, if there are any, and hash them. Also tally the number
    of gen txs in the block.
    """
    """"""
    heightOfBlockchain = getHeightOfBlockchain()
    
    possibleGenesisTxs = returnNonCoinbaseTxs(startBlock)
    if(possibleGenesisTxs == None):
        print('Start block not the genesis tx\'s block...')
        return

    """ 
    txCountTrack    - used to construct the punchcard to be returned
                      e.g. [2,3] represents 2 gen txs, and 3 in the subsequent block
    rawTxs          - stores the raw txs to be hashed, so that the next block txs 
                      can be verified
    genFound        - boolean tracking if a gen tx has been found
    countTxs        - counts the number of txs in a block that are part of the same
                      POF chain
    """
    txCountTrack = []
    rawTxs = []
    genFound = False
    countTxs = 0

    for tx in possibleGenesisTxs['txids']:
        method = 'getrawtransaction'
        ret = instruct_wallet(method, [tx, True, possibleGenesisTxs['blockhash']])
        """from what I can tell the custom output is the 1st of the > 1 that exist"""
        rawTxOutputs = ret['result']['vout'][0]
        print(method,':\n', ret,'\n')

        if(GENESIS_STRING in rawTxOutputs['scriptPubKey']['hex']):
            genFound = True
            countTxs = countTxs + 1
            rawTxs.append(ret['result']['hex'])

    if(genFound == False):
        print('No genesis tx found')
        return
    
    txCountTrack.append(countTxs)

    """ Hash the gen txs"""
    hashedTxs = hashlib.sha256(bytes(str(rawTxs), 'utf-8')).hexdigest()
    print(hashedTxs)


    """"""
    """
    Scanning the subsequent blocks until a block with no POF txs is found.
    
      - This condition is subject to change, but would require significantly
        more runtime to search all block in range [startBlock + 1, heightOfBestBlock]
    """
    """"""
    rawTxs = []
    nextPOFBlockFound = False
    countTxs = 0
    for blockIndex in range(startBlock + 1, heightOfBlockchain + 1):
        nonCoinbaseTxs = returnNonCoinbaseTxs(blockIndex)
        if(nonCoinbaseTxs == False):
            print("br1")
            break
        
        for tx in nonCoinbaseTxs['txids']:
            method = 'getrawtransaction'
            ret = instruct_wallet(method, [tx, True, nonCoinbaseTxs['blockhash']])
            rawTxOutputs = ret['result']['vout'][0]
            print(method,':\n', ret,'\n')

            if(hashedTxs in rawTxOutputs['scriptPubKey']['hex']):
                nextPOFBlockFound = True
                countTxs = countTxs + 1
                rawTxs.append(ret['result']['hex'])
        
        if(nextPOFBlockFound == False):
            print("br2")
            break
        
        hashedTxs = hashlib.sha256(bytes(str(rawTxs), 'utf-8')).hexdigest()
        print(hashedTxs)

        txCountTrack.append(countTxs)
        """ Reset the list and boolean for another iteration"""
        rawTxs = []
        nextPOFBlockFound = False
        countTxs = 0
    
    print("The resultant punchcard: ", str(txCountTrack))



""" Just for testing: 
        - 1665/1667 should failure
        - 1666 should pass
"""
scanChain(359)