import base64
from email.encoders import encode_base64
from hashlib import sha256
from django.test import TestCase

#from .models import User

# Create your tests here.

'''
class PaymentUnitTest(TestCase):

    def test_has_paid(self):
        user=User.objects.create(username="test")
        user.save()

        self.assertFalse(user.has_paid(),"Intial user shoud  have empty paid_until attr")
        
'''
import json,pickle

def readFile():

    data={}
    s=''

    geeky_file = open('C:/Users/dell/OneDrive/Project/Inq/website/inq/account_details.pkl', 'rb')

    #dict=pickle.load(geeky_file)


    while True:
        try:
            s=(pickle.load(geeky_file))
            x=list(s.keys())[0]
            
            data[x]=s
            

            
        except EOFError:
            break

    
        
        
    geeky_file.close()

    
    print(data)

    
    username='mkd@345'

    #acc=dict[username]['Account_Address']

    #print('acc',acc)

    return(data)


    
  


  

    


readFile()

import requests
import hashlib
import razorpay




def test_upi():

    key_id='rzp_test_ZkRCKCR0sXpizq'

    key_secret="dj2pWfu7LkVmvab2iE122ykR"
    
    client=razorpay.Client(auth=(key_id,key_secret))
    headers = {
        
        "Content-Type": "application/json",
        "vpa":"6393168377@ybl",
        "Accept":"application/json",
        "Authorization":"Basic "+encode_base64(key_secret)
       
        
    
    }


    
    

    url = "https://api.razorpay.com/v1/payments/validate/vpa"

    payload = {}
    
    response = requests.post(url, headers=headers)

    print(response.text)


#test_upi()





from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.validations import Validations

def test_upi_cashfree():

    client_id='CF185486CB2U8GM7ILBNF68P87SG'
    client_secret='df98abe026f0b4c63f37c1f273f9b36f52281277'

    env='PROD'

    Payouts.init(client_id,client_secret,env)

    BANK_VALID=Validations.bank_details_validation(
        

        name="Aayush Dwivedi",
        phone="6393168377",
        bankAccount="39774209232",
        ifsc="SBIN0001494"
    )



#test_upi_cashfree()  

def upi_pe():
    url = "https://mercury-uat.phonepe.com/v3/vpa/MERCHANTUAT/6393168377@ybl/validate"

   


    headers = {
        
        "Content-Type": "application/json",
        
        "Accept":"application/json",
        "X-VERIFY":x
       
        
    
    }

    response = requests.get(url, headers=headers)

    print(response.text)





    

#upi_pe()


#


