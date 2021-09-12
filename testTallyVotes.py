from src.tallyVotes import tallyVotes
from src.scanForPOFChain import scanForPOFChain
import functools 

resultantPunchcard = scanForPOFChain(601)

# here we wanna go from [[3, '00'], [2, 'ff'], [2, '00'], [4, 'ff'], [5, 'ff']] to ['00', 'ff', ...]
extractedVotes = list(map(lambda x: x[1], resultantPunchcard))

""" This sample run is a vote for who the Satoshi Nakamoto is... """
candidates = ['Nick Szabo', 'Hal Finney', 'Ian Grigg']

print(tallyVotes(extractedVotes, candidates))