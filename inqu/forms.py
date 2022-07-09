from django import forms  
class BankForm(forms.Form):  
    firstname = forms.CharField(label="Name in bank",max_length=50)  
    bank = forms.CharField(label="Bank",max_length=50) 
    accno1 = forms.CharField(label="Account",max_length=50) 
    accno2 = forms.CharField(label="Retype Account",max_length=50) 
    ifsc = forms.CharField(label="IFSC CODE",max_length=50) 
   
      
    
    bankstatement      = forms.FileField(label="Bank Statement") # for creating file input  
    incomeproof      = forms.FileField(label="Income proof") # for creating file input  