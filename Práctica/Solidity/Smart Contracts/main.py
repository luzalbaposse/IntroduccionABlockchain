import web3 as web3
import dotenv as dotenv
import os as os
import utils
import datetime
import time as time

rpc = os.environ["ETHEREUM"]
web3 = web3.Web3(web3.HTTPProvider(rpc))
if web3 == None:
    print("Web3 is not connected")
    exit(1)
else: 
    print("Web3 is connected")

lastBlockNumber = web3.eth.blockNumber
print("Last block number: ", lastBlockNumber)
print("Last block hash: ", web3.eth.getBlock(lastBlockNumber).hash.hex())

## TIME STAMP
timestamp = web3.eth.getBlock(lastBlockNumber).timestamp
print("Timestamp: ", timestamp)

## DATE TIME
datetime_object = datetime.datetime.fromtimestamp(timestamp)
print("Date time: ", datetime_object)


