
from ctypes.wintypes import PINT
from dis import Bytecode
from pickle import bytes_types
from solcx import compile_standard,install_solc

import json

with open("C:/Users/dell/OneDrive/Project/Inq\website/inq\solidity_code/Multi.sol",'r') as file:
    Multi_file=file.read()





install_solc("0.6.0")
#print("Installing......")



compiled_sol=compile_standard(

{
    "language":"Solidity",
    "sources":{"Multi.sol":{"content":Multi_file}} ,
    "settings":{
        "outputSelection":{
            "*":{"*":["abi","metadata","evm.bytecode","evm.sourceMap"]}
                
            
        }
    },
},
solc_version="0.6.0",
)





with open ("compiled_sol.json",'w') as file:
    json.dump(compiled_sol,file)


bytecode=compiled_sol['contracts']['Multi.sol']['Mutli']['evm']['bytecode']['object']


abi=compiled_sol['contracts']['Multi.sol']['Mutli']['abi']


print('okkk')

from web3 import Web3
ganache_url="HTTP://192.168.29.185:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))

contract_address='0xa69CaDfB1c3Fa2Bb4e631F58Bf6f90C9B7849e35'
chainid=1337
privatekey='0x079671bf2829256991c5572205c96a2a9627ec1f17235c6652f71669872c4fe7'


Multi=web3.eth.contract(abi=abi,address=contract_address)

print(Multi)


#get latest transacion

nonce=web3.eth.getTransactionCount(contract_address)
print(nonce)


#transaction=Multi.constructor().buildTransaction({"chainId":chainid,'from':contract_address,"nonce":nonce})
#print(transaction)

#txn_hash=web3.eth.send_transaction({
  #'to': '0xc806768Ee5F30766BBE3D29f896ac09d121Cb57E',
  #'from': contract_address,
  #'value': 10})

#print(web3.eth.get_transaction('0xc015f5fc0d7491f62e4568253433ff0c8e00e6fab0b7b9127768b4eda91ce948'))

x=Multi.functions.addPlayer('Ayd','Dwi').transact()
print(x)