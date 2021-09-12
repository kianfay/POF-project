# POF-project
Playing around with bitcoin and a proof of transaction consensus for arbitrary voting. A trivial approach to creating 
a hash chain inside the bitcoin blockchain, where essentially, the largest batch of transactions is officially 
the most relevant next link in the chain.

Usage:
- Start an instance of bitcoind running in regtest mode on your local machine
- Run a sample flow using python3, with the votes passed as parameters in the test file: `python3 testRunCustomChain.py`
- Scan the Proof Of Flow chain that was just created using with a group of candidates : `python3 testScanForPOFChain.py`
- Tally the votes : `python3 testTallyVotes.py`

