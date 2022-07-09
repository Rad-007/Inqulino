


#from ast import arg
from . block_test import *

import datetime,time
#from apscheduler.schedulers.background import BackgroundScheduler
#import schedule
import threading
def subscribe(address,type_m,amount,private_key):

    


    

    '''

    try:

        while True:

            currenttime=datetime.datetime.now().replace(microsecond=0)
            timea=time+datetime.timedelta(minutes=3)
            
            if (timea==currenttime) and type_m=='Yearly':

                print("Lending started")
                tx_lend=block_test.lend(account_1=address,amount=amount,private_key=private_key)
                print(tx_lend)
                
        
    
            if (timea==currenttime) and type_m=='borrow':

                print("Borrowing started")
                tx_borrow=block_test.borrow(account_2=address,amount=amount)
                print(tx_borrow)

               
    
    except KeyboardInterrupt:
        pass

sched = BackgroundScheduler()

    sched.add_job(block_test.lend,trigger='interval', args=(address,amount,private_key),minutes=2)
    
    sched.start()
    print("Done")


    schedule.every(2).minutes.do(block_test.lend,account_1=address,amount=amount,private_key=private_key)

    while 1:
        schedule.run_pending()
        time.sleep(1)
    



    '''
    print(time.ctime())
    txn=lend(address,amount,private_key)
    print(txn)



    if type_m=='Yearly':

        threading.Timer(31536000,subscribe,args=(address,type_m,amount,private_key)).start()

    if type_m=='Half-Yearly':

        threading.Timer(15811200,subscribe,args=(address,type_m,amount,private_key)).start()
    
    if type_m=='Quaterly':

        threading.Timer(10368000,subscribe,args=(address,type_m,amount,private_key)).start()
    
    if type_m=='Monthly':

        threading.Timer(2592000,subscribe,args=(address,type_m,amount,private_key)).start()

    if type_m=='Daily':

        threading.Timer(86400,subscribe,args=(address,type_m,amount,private_key)).start()


    return(txn)
    




#address='0xa69CaDfB1c3Fa2Bb4e631F58Bf6f90C9B7849e35'
#private_key='0x079671bf2829256991c5572205c96a2a9627ec1f17235c6652f71669872c4fe7'
#amount=1
#type_m='Yearly'

#subscribe(address,type_m,amount,private_key)       
        
        




