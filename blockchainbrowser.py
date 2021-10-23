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


# Add your own url details in here.
provider_url = 'https://mainnet.infura.io/v3/XXXXXX'


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
    print(' 0.1.                             ')
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

# Returns the current gas price in Wei.


def gasPrice():
    gasprice = w3.eth.gasPrice
    return gasprice


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
                        action='store_true', help='Get the latest gas price')
    parser.add_argument('-gc', '--gettransactioncount',
                        help='Get the transaction count')
    parser.add_argument('-k', '--konnection', action='store_true',
                        help='Check the connection to the blockchain')
    parser.add_argument('-m', '--make', help='Make a transaction')
    parser.add_argument('-s', '--sign', help='Sign a transaction')

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
        print('--> Gas price:', gasPrice())
    elif args.address:
        print('--> Checking the balance of address:', args.address)
        print('--> Balance:', w3.fromWei(checkBalance(args.address), 'ether'))
    elif args.block:
        print('--> Looking up block:', args.block)
        print('--> Block details:', lookupBlock(args.block))
    elif args.konnection:
        print('--> Checking to see if we are konnected to the blockchain\n')
        checkConection()


if __name__ == '__main__':
    banner()
    main()
