

from web3 import Web3

ganache_url="http://192.168.29.185:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))


def isAddress(address):
    return (web3.isAddress(address))

def lend(account_1,amount,private_key):
    
#Tutorial Code Goes Here..
    
    
    account_2="0xc806768Ee5F30766BBE3D29f896ac09d121Cb57E"
    #private_key="fad035698bbcc8e53be4e9f33b8ab2b01c31efea0dd46776f63b94deb1819df5"
    nonce=web3.eth.getTransactionCount(account_1)
    
    print(web3.isConnected())

    
    tx={
        'nonce': nonce,
        'to': account_2,
        'value': web3. toWei(amount, 'ether'),
        'gas': 200000,
        'gasPrice': web3.toWei('50', 'gwei')

    }


    if check_balance(account_1)>amount:
        signed_tx=web3.eth.account.signTransaction(tx, private_key)
        tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return(web3. toHex(tx_hash))
    else:
        return("Insufficient balance")
    




#lend()

import json

def borrow(account_2,amount):
    print(isAddress(account_2))


    
    account_1="0xd34eFe2bD22237487C51E789e65561dd7e97b9A9"
    #account_2="0xDdf40da63Bb248d4364F5a942CF3F46B684e6F58"
    private_key="0x24abc5f4fe893dda0d8ba5ad889a6728fc39725d6219ab58ec0589571343a562"
    nonce=web3.eth.getTransactionCount(account_1)
    print(nonce)

    #amount=input("Enter amount:")
    tx={
        'nonce': nonce,
        'to': account_2,
        'value': web3. toWei(amount, 'ether'),
        'gas': 200000,
        'gasPrice': web3.toWei('50', 'gwei')

    }
    signed_tx=web3.eth.account.signTransaction(tx, private_key)
    tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return(web3. toHex(tx_hash))




#print("Borrow")

#borrow()


def New_account(name,username,password):

    
    account={}
    user={}
    acc_address=[]
    acc_private_key=[]


    
    acc=web3.eth.account.create()
        
    user['Name']=name
    user['username']=username
    user['Account_Address']=acc.address
    user['private_key']=acc.privateKey
    user['password']=password

    account[username]=user

    accountinfo=[acc.address,acc.privateKey]


        
    with open('account_details.txt', 'a') as convert_file:

        convert_file.write(str(account)+'\n')
        
        

    
    return accountinfo
    


#accounts()
#print("Account\n\n")

def check_balance(address):


    wallet=web3.eth.get_balance(address)
    wallet=wallet/1000000000000000000

    print(wallet)
    return(wallet)







#check_balance('0x8c9e9D99aA384202E250051018D57dA984ec6aC8')