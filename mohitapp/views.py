from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from mohitapp.models import cart
from django.http import HttpResponseRedirect
import random, string
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def nott(request):
    return render(request,'not.html')


def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def proj(request):
    return render(request,'project.html')






def ende(request):
    if request.method == "POST":
        user_input=request.POST['txt']
        opt=request.POST['option']
        output=cryp(user_input,opt)
        messages.info(request,output)
        print('the option selected is',opt,'output >',output)
        return HttpResponse(output)
    return render(request,'ende.html')
    


def cryp(input,opt):
    chars= ' 1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=_.,;/'
    chars =list(chars)
    key = '1q2w3e4r5t6y7u8i9o0pazsxdcfvgbhnjmk,l.;/ !@#$%^&()_+-=*AQSWDEFRGTHYJUKILOZPMXNCBV'
    key=list(key)

    text=input
    ctxt=''
    c=opt
    if c=="Encryption":
        for i in text:
            inde= chars.index(i)
            ctxt+= key[inde]
    else:
        for i in text:
            index= key.index(i)
            ctxt+= chars[index]

    return ctxt