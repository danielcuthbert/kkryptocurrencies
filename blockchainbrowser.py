#!/usr/bin/python3

# Python3 blockchain explorer
# A work in progress
# 0.1
# Daniel Cuthbert
# https://web3py.readthedocs.io/en/stable/web3.eth.html

# Set up the connection to the blockchain using Infura.io
from web3 import Web3
import argparse
import sys
import json
import requests


# Add your own url details in here.
provider_url = 'https://mainnet.infura.io/v3/xxxxx'

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]')


# initialize the web3 object
w3 = Web3(Web3.HTTPProvider(provider_url))




private_key = ""
tx = {
    'nonce': '',
    'gasPrice': w3.toWei('100', 'gwei'),
    'gas': '100000',
    'to': '',
    'value': w3.toWei(1, 'ether'),
}


class colours:
    ERROR = '\033[91m'
    OK = '\033[92m'
    DEFAULT = '\033[94m'


def banner():
    print('\n')
    print('__________________________________')
    print(' Ethereum Explorer                ')
    print(' 0.3.                             ')
    print(' @danielcuthbert                  ')
    print('__________________________________')
    print('      \                           ')
    print('       \                          ')
    print('         ^__^                     ')
    print('         (oo)\_______             ')
    print('         (__)\       )\/\         ')
    print('             ||----w |            ')
    print('             ||     ||            ')
    print('\n                                ')

# check the connection


def checkConection():
    if w3.isConnected() == True:
        print(f"{colours.OK}--> We are cryptoing baby!{colours.OK}")
    else:
        print(f"{colours.ERROR}--> Arse, we are not cryptoing!{colours.ERROR}")


# Returns the transaction specified by transaction_hash. 
# If the transaction has not yet been mined throws web3.exceptions.TransactionNotFound
def getTransaction(transaction_hash):
    transaction = w3.eth.getTransaction(transaction_hash)
    return transaction

# get the number of transactions sent from an account


def getTransactionCount(account_id):
    transactionCount = w3.eth.getTransactionCount(account_id)
    return transactionCount

# Returns the block specified by block_identifier


def getLatestBlock():
    latestBlock = w3.eth.get_block_number()
    return latestBlock


# The process to lookup a block by number
def lookupBlock(blockNumber):
    block = w3.eth.get_block(blockNumber)
    print(block)

# The process to check the balance of an address


def checkBalance(address):
    balance = w3.eth.getBalance(address)
    return balance

#
# Sending a transaction needs a few things, namely an address, a value, and a gas price and a nonce
# The nonce is the number of transactions sent from the address in the last block
# The gas price is the price of gas in wei
# The value is the amount of ether to send
# The address is the address to send the ether to
# The transaction hash is the hash of the transaction
# The transaction receipt is the receipt of the transaction
#


def makeTransaction(address, amount):
    # Eth.send_raw_transaction(raw_transaction) might be a better approach
    w3.eth.sendTransaction({'to': address, 'value': amount})
    return True

# The process to lookup a transaction by hash


def lookupTransaction(transactionHash):
    transaction = w3.eth.getTransaction(transactionHash)
    return transaction

# The process to lookup up receipt of a transaction by hash


def lookupReceipts(receipts):
    receipt = w3.eth.getTransactionReceipt(receipts)
    return receipt

# The process to sign a transaction


def signTransactions(private_key, tx):
    signed = w3.eth.account.signTransaction(tx, private_key)
    return signed

# Returns the current gas price in Wei and prices for transfers


def gasPrice():
    gasprice = w3.eth.gasPrice
    rq = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
    data = json.loads(rq.content)
    print("The current gas price in Wei is", gasprice)
    print("A safe and low transfer will cost you", data['safeLow'], "GWEI")
    print("A standard transfer will cost you", data['average'], "GWEI")
    print("A fast transfer will cost you", data['fast'], "GWEI")

    


# Smart contract search
# We need to know the address of the contract, account number and the contracts ABI
# You need to add a .call to the end of the function to make it a call

def smartContractSearch(contract_address): 

    contract = w3.eth.contract(address=contract_address, abi=abi)
    contractSupply = contract.functions.totalSupply().call()
    print('--> Total Supply is', contractSupply)  
    print('--> Contract Name is', contract.functions.name().call())
    print('--> Symbol is', contract.functions.symbol().call())
    



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address',
                        help='Address to check the balance of')
    parser.add_argument(
        '-b', '--block', help='Returns the block specified by block_identifier')
    parser.add_argument('-g', '--getblock',
                        action='store_true', help='Get the latest block')
    parser.add_argument('-gt', '--gettransaction',
                        help='Get a transaction from a hash')
    parser.add_argument('-gp', '--gasprice',
                        action='store_true', help='Get the latest gas price and average fees')
    parser.add_argument('-gc', '--gettransactioncount',
                        help='Get the transaction count')
    parser.add_argument('-k', '--konnection', action='store_true',
                        help='Check the connection to the blockchain')
    parser.add_argument('-m', '--make', help='Make a transaction')
    parser.add_argument('-s', '--sign', help='Sign a transaction')
    parser.add_argument('-c', '--contract', help='Lookup a smart contract')

    args = parser.parse_args()
    if args.getblock:
        print('--> Latest Block:', getLatestBlock())
    elif args.gettransaction:
        print('--> Getting transaction:', args.gettransaction)
        print('--> Transaction:', lookupTransaction(args.gettransaction))
    elif args.gettransactioncount:
        print('--> Getting transaction count:',
              getTransactionCount(args.gettransactioncount))
    elif args.gasprice:
        gasPrice()
    elif args.address:
        print('--> Checking the balance of address:', args.address)
        print('--> Balance:', w3.fromWei(checkBalance(args.address), 'ether'))
    elif args.block:
        print('--> Looking up block:', args.block)
        print('--> Block details:', lookupBlock(args.block))
    elif args.konnection:
        print('--> Checking to see if we are konnected to the blockchain\n')
        checkConection()
    elif args.contract:
        print('--> Looking up smart contract:', args.contract)
        print('--> Smart contract supply:', smartContractSearch(args.contract)) 


if __name__ == '__main__':
    banner()
    main()
