
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="Inqulino",
  user="Aayush",
  password="Inq@ulino1234",
  
)



mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE account")

mycursor.execute("CREATE TABLE Account Details (username VARCHAR(255) PRIMARY KEY, address VARCHAR(255), privatekey VARCHAR(255), password VARCHAR(255))")


'''
import rsa
publicKey, privateKey = rsa.newkeys(250)
msg=b'grtcgv'

def encrypt(s,publicKey,privateKey):

    

    print("Public",publicKey)
    print("Private",privateKey)
    print('\n\n')
 
# this is the string that we will be encrypting
    message = s

    encMessage = rsa.encrypt(message.encode(),
                         publicKey)
    
    msg=encMessage

    print("original string: ", message)
    print("encrypted string: ", encMessage)
    
    return(encMessage.hex())

    


def decrypt(s):

    decMessage = rsa.decrypt(s, privateKey).decode()
 
    print("decrypted string: ", decMessage)








# IN CSV

import  csv

import os.path
def createDatabase(username,address,privateKey,password):


    


    filename='accounts.csv'

    fields=['Username','Address','Private_Key','Password']

    rows=[[f'Username={username}',f'Address={address}',f'Private_Key={privateKey}',f'Password={password}']]

    

    with open(filename,'a') as csvfile:
        csvwriter=csv.writer(csvfile)

        if os.path.exists(filename):
            csvwriter.writerows(rows)
        else:

            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        




#encrypt("Hello Aayush",publicKey,privateKey)


#print(type(b'\x00\xdar^\xf4\xd5\x1d\xc7\xeft\x94\xfdi\xeb~\x15\x9d\xd2\xee]\x91\\\xa7\x17\xb5eg\xf3d\xfd\n\xbd'))

#decrypt(s=msg)


#createDatabase('a11','ee13a363','0x153fabc','a1we2')
#createDatabase('a11857','ee13a3635454','0x153fabchg','a1we9896')