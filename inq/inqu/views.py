
from typing import Any
from unittest import result
from webbrowser import get
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, TemplateView

from . models import  *
#import razorpay
from inq import settings
import requests
import json
import stripe

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


import os
# Create your views here.

from .block_test import *
from inqu import block_test

import json
import requests

def price_rate():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    
    # Making list for multiple crypto's
    currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT","ETHUSDT","BCHUSDT","BTGUSDT","DASHUSDT","XRPUSDT","ZECUSDT"]
    j = 0

    price={}
    
    # running loop to print all crypto prices
    for i in currencies:
        
        # completing API for request
        url = key+currencies[j]  
        data = requests.get(url)
        data = data.json()
        j = j+1

        price[data['symbol']]=round(float(data['price']),2)
        
    return (price)

def index (request):
    data=[]
   
  
# Defining Binance API URL
    




    
    
    return render(request,'index.html',context=price_rate())


def pricing (request):
    

    return render(request,'pricing.html',context=price_rate())


def faq (request):
    

    return render(request,'faq.html',context=price_rate())


def blog (request):
    

    return render(request,'blog.html',context=price_rate())

def error (request):
    

    return render(request,'404.html')


def pay (request):
    

    return render(request,'pay.html')


def team (request):
    

    return render(request,'team.html',context=price_rate())

def charts (request):
    

    return render(request,'charts.html',context=price_rate())






def profile(request):

    username=str(request.user)
    
    
    #print("Username",username)

    f=open('transaction_details.txt','r')

    dict=readFile()

    #print(dict)




    l=[]
    acc=dict[username]['Account_Address']

    balance=check_balance(acc)
    pri=dict[username]['private_key'].hex()

    for line in f:

        if username in line:

            print(line)

            #dict=readFile()
            #address=dict[username]['address']
            

            

            

        
            d={}

            

            x=line.split(':')

            if 'borrow' in x[2]:

                d['type']='borrow'
                d['Name']='Inqulino Borrow'
                d['address']='0x0C47acAF2177A385c899B15fd2E2731ef23be4b3'+'   '
            
            else:
                d['type']='lend'
                d['Name']='Inqulino Lend'
                d['address']='0x8c9e9D99aA384202E250051018D57dA984ec6aC8'


            date=x[3][19:42].replace(',','').split()

            date=date[2]+'/'+date[1]+'/'+date[0]

            d['date']=date

            i=x[4].index(',')

            am=x[4][:i]

            d['amount']='  '+str(am)+' eth'

            id=x[5][2:-4]

            

            d['transaction_id']=id

            l.append(d)
    

    #print(l)

    context={'l':l,
             'acc':acc,
             'private_key':pri,'balance':balance}



    print('njn',context)
        

        




    return render(request,'profile.html',{"context":context})
         


from .database import createDatabase    


import json
import ast
import pickle
def readFile():

    """
  
# reading the data from the file
    with open('account_details.txt','r') as f:
        data = f.read()
    
    #print("Data type before reconstruction : ", type(data))
        
    # reconstructing the data as a dictionary
    d = ast.literal_eval(data)
    
    return d
    """


    
    geeky_file = open('account_details.pkl', 'rb')

    dict=pickle.load(geeky_file)




    
        
        
    geeky_file.close()
    #print(dict)

    return(dict)
  
    








         
def signin(request):


    data=open('data.txt','a')
    if request.method=='POST':
        name=request.POST['name']
        
        username=request.POST['username']
        email=request.POST['email']
        
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        data.write(name+"  "+username+"  "+password1+"\n")

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exits')
                return redirect('signin')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exits')
                return redirect('signin')
            
            else:
                
                acc=block_test.New_account(name=name,username=username,password=password1)
                user=User.objects.create_user(username=username,email=email,password=password1)
                #createDatabase(username=username,address=acc[0],privateKey=acc[1],password=password1)
                user.save()
                #accounts(username,password1)
                #messages.info("Signup Complete !  Login Now")
                return redirect('login')
        
        else:
            #messages.info("Passwords not same")  
            return redirect ('signin')
    else:
        return render(request,'signup.html',context=price_rate())  


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            return redirect ('login') 
            #messages.info("Incorrect Password")
            
        
        
    else:

        return render(request,'login.html',context=price_rate())



def eth_borrow(request):

    
    print(block_test.web3.isConnected())

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        address=request.POST['address']
        amount=request.POST['amount']

        

        


        user=auth.authenticate(username=username,password=password)


        if user is not None and block_test.isAddress(str(address)):
            js={}
            details={}


            #js[username]['type']='borrow'
            #js[username]['time']=

            convert_file= open('transaction_details.txt', 'a')
            

            auth.login(request,user)

            txn=block_test.borrow(str(address),float(amount))
            print(txn)

            details['type']='borrow'
            details['amount']=amount
            details['Start_time']=datetime.datetime.now().replace(microsecond=0)
            details['transaction id']=txn

            js[username]=details

            convert_file.write(str(js)+'\n')

            print("Transaction done")
            print(txn)


            return redirect('pricing')

        else:
            return redirect('eth_borrow')

    else:

        return render(request,'eth_borrow.html')






from sol_py import subscribe

import datetime

def eth_lend(request):
    print(block_test.web3.isConnected())

    

    


    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        method=request.POST['method']
        amount=request.POST['amount']
        address=request.POST['account_address']
        privateKey=request.POST['private_key']



        ds=readFile()
        
        print(ds)

        print("File")


        user=auth.authenticate(username=username,password=password)

        print(method)
        
        

        


        convert_file=open('transaction_details.txt', 'a') 
            

        if user is not None  :

           
           
            if verify_private_key(address=address,private_key=privateKey):
                print("ADDRESS",address)
                print("Private_Key",privateKey)
                print("\n\n")

                js={}
                details={}

                details['type']='lend'
                details['amount']=amount
                details['Start_time']=datetime.datetime.now().replace(microsecond=0)
                print("Lending started")

                
                


                txn=subscribe.subscribe(address=address,type_m=method,amount=amount,private_key=privateKey)

                details['transaction id']=txn


                js[username]=details

                convert_file.write(str(js)+'\n')
                


                

                




                return redirect('pricing')
            else:
                return render(request,'eth_lend.html',{'msg':'Private Key does not maches with account address'})

        else:
                return redirect('eth_lend',{'msg':'Invalid username or password'})

    else:

            return render(request,'eth_lend.html')

        








def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk):
    return render (request,'post.html',{'pk':pk})


def contact(request):

    #return(request,'contact.html')

    
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['message']

        message=open("message.txt",'a')
        message.write(name+'  \n')
        message.write(email+'  \n')
        message.write(subject+'  \n')
        message.write(msg+'  \n------------------')
        return redirect('/')


    else:

        return render(request,'contact.html',context=price_rate())


def borrow(request):

    #return(request,'contact.html')

    
    
    if request.method=='POST' and request.FILES['bankstatements'] and request.FILES['incomeproofs'] and request.FILES['pan']:

        name=request.POST['name']
        bank=request.POST['bank']
        accno1=request.POST['accno1']
        accno2=request.POST['accno2']
        ifsc=request.POST['ifsc']
        upiid=request.POST['upiid']

        bankstatement=request.FILES['bankstatements']
        incomeproof=request.FILES['incomeproofs']
        pan=request.FILES['pan']
        
        fs=FileSystemStorage()
        
        
        

        if accno1==accno2:

            details=open("Details.txt",'a')

            d={'Name':name, 'bank':bank, 'accno':accno1, 'ifsc':ifsc, 'upi':upiid }
            details.write(str(d)+"\n\n")
            file1=fs.save(name+" "+bankstatement.name,bankstatement)
            file2=fs.save(name+" "+incomeproof.name,incomeproof)
            file3=fs.save(name+" "+pan.name,pan)
            messages.info(request,'Details  submitted')
            

            return redirect('pricing')
        else:
            messages.info(request,'Account number not same')

            return redirect ('borrow')
    
    else:
        return render(request,'borrow.html',context=price_rate())
        


def lend(request):

    #return(request,'contact.html')

    
    
    if request.method=='POST' and request.FILES['bankstatements'] and request.FILES['incomeproofs'] and request.FILES['pan']:

        name=request.POST['name']
        bank=request.POST['bank']
        accno1=request.POST['accno1']
        accno2=request.POST['accno2']
        ifsc=request.POST['ifsc']
        upiid=request.POST['upiid']

        bankstatement=request.FILES['bankstatements']
        incomeproof=request.FILES['incomeproofs']
        pan=request.FILES['pan']
        
        fs=FileSystemStorage()
        
        
        

        if accno1==accno2:

            details=open("Details.txt",'a')

            d={'Name':name, 'bank':bank, 'accno':accno1, 'ifsc':ifsc, 'upi':upiid }
            details.write(str(d)+"\n\n")
            file1=fs.save(name+" "+bankstatement.name,bankstatement)
            file2=fs.save(name+" "+incomeproof.name,incomeproof)
            file3=fs.save(name+" "+pan.name,pan)
            messages.info(request,'Details  submitted')
            

            return redirect('eth_lend')
        else:
            messages.info(request,'Account number not same')

            return redirect ('lend')
    
    else:
        return render(request,'lend.html',context=price_rate())





    
def phonepe(request):
    url = "https://mercury-uat.phonepe.com/v3/debit"

    headers = {
        "Accept": "text/plain",
        "Content-Type": "application/json",
        "X-CALLBACK-URL": "https://www.demoMerchant.com/callback"
    }

    response = requests.request("POST", url, headers=headers)

    print(response.text)
    return render(request,'pay.html')



def razorclient(request):

    if request.method=='POST':
    

        razorpay_client = razorpay.Client (auth=(settings.razorpay_id, settings.razorpay_key))
        razorpay_pay=razorpay_client.order.create(dict(amount=1000,currency='INR',receipt=1,payment_capture='0'))
        print('razorpay order id',razorpay_pay['id'])

        return render(request,'/')
    else:
        return HttpResponse('Error')




class ProductListView(ListView):
    model = Product
    template_name = "payments/product_list.html"
    context_object_name = 'product_list'


class ProductCreateView(CreateView):
    model = Product
    template_name = "payments/product_detail.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context  


class ProductDetailView(DetailView):
    pass

@csrf_exempt


def create_checkout_session(request):
    if request.method=="GET":

        try:
            prices = stripe.Price.list(
                lookup_keys=[request.form['lookup_key']]
                
            )

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': prices.data[0].id,
                        'quantity': 1,
                    }
                ],
                mode='subscription',
                success_url=YOUR_DOMAIN +
                '/success.html?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=YOUR_DOMAIN + '/cancel.html'
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            print("Exception",e)
            return  redirect('pay')
    
    else:
        print(request.method)
        return HttpResponse('Error')


def customer_portal(request):
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    checkout_session_id = request.form.get('session_id')
    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    return_url = YOUR_DOMAIN

    portalSession = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url,
    )
    return redirect(portalSession.url, code=303)


def webhook_received(request):
    # Replace this endpoint secret with your endpoint's unique secret
    # If you are testing with the CLI, find the secret by running 'stripe listen'
    # If you are using an endpoint defined with the API or dashboard, look in your webhook settings
    # at https://dashboard.stripe.com/webhooks
    webhook_secret = 'whsec_12345'
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    print('event ' + event_type)

    if event_type == 'checkout.session.completed':
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.subscription.trial_will_end':
        print('Subscription trial will end')
    elif event_type == 'customer.subscription.created':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.updated':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.deleted':
        # handle subscription canceled automatically based
        # upon your subscription settings. Or if the user cancels it.
        print('Subscription canceled: %s', event.id)

    return jsonify({'status': 'success'})









    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    order = OrderDetail()
    order.customer_email = request_data['email']
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price * 100)
    order.save()

    # return JsonResponse({'data': checkout_session})
    #return JsonResponse({'sessionId': checkout_session.id})
    return render (request,'stripe_check.html')
	


class PaymentSuccessView(TemplateView):
    template_name = "payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(OrderDetail, stripe_payment_intent=session.payment_intent)
        order.has_paid = True
        order.save()
        return render(request, self.template_name)

class PaymentFailedView(TemplateView):
    template_name = "payment_failed.html"

class OrderHistoryListView(ListView):
    model = OrderDetail
    template_name = "order_history.html"



from django.views.generic.base import TemplateView



stripe.api_key = settings.STRIPE_SECRET_KEY 
class HomePageView(TemplateView):
    template_name = 'stripe_check.html'

    


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Lend',
            source=request.POST['stripeToken']
        )
        return render(request, 'stripe_check.html')
    
    else:
        return HttpResponse("Error")

YOUR_DOMAIN = 'http://localhost:4242'
#from .models import Price
from django.views import View


class LandingPageView(TemplateView):
    template_name="landing.html"


def get_context_data(self, **kwargs:Any): # new
        context = super(LandingPageView,self).get_context_data(**kwargs)
        context.update ({
            "STRIPE_PUBLIC_KEY":settings.STRIPE_PUBLISHABLE_KEY
        })
        return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 20000,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN +
            '/success/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id':checkout_session.id
        })



