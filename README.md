# POF-project
Playing around with bitcoin and a proof of transaction consensus for arbitrary voting. A trivial approach to creating 
a hash chain inside the bitcoin blockchain, where essentially, the largest batch of transactions is officially 
the most relevant next link in the chain.

Usage:
- Start an instance of bitcoind running in regtest mode on your local machine
- Run the program using python3 (e.g. python3 addingnextblocktx.py)
