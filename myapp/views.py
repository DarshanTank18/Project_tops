from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from BATCHPROJECT import settings

# Create your views here.

def index(request):
    person = request.session.get('cuser')
    return render(request,'index.html',{'person':person})

def userlogin(request):
    msg=""
    if request.method == 'POST':
        mail = request.POST['email']
        pas = request.POST['password']

        user = signuptbl.objects.filter(email = mail, password = pas)

        if user:
            print("Login sucess")
            request.session['cuser'] = mail
            return redirect('/')
        else:
            print("Error")
            msg = "Error!Login faild..."
    return render(request,'userlogin.html',{'msg':msg})

def usersignup(request):
    msg = ""
    global newreq
    if request.method == 'POST':
        newreq = signupform(request.POST)
        if newreq.is_valid():
            print("Login sucess....")
            
            #Email Sending Code
            global otp
            otp=random.randint(1111,9999)
            sub="Your One Time Password"
            msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time otp is {otp}.\n\nThanks & Regards!\n+91 95869 74648 | darshancollege123@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                
            return redirect('otp')
        else:
            print(newreq.errors)
    return render(request,'usersignup.html',{'msg':msg})

def perlogout(request):
    logout(request)
    return redirect('Login')

def contectus(request):
    person = request.session.get('cuser')
    if request.method == 'POST':
        newreq = contectForm(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Mail sent done...")

            sub="thanks for connect us"
            msg=f"Hello User!\n\nThanks for Contact Us.\n\nThanks For connect us..\n\nwe will connect soon.\n\n+91 95869 74648 | darshancollege123@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['mail']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
        else:
            print(newreq.errors)
    return render(request,'contect.html',{'person':person})

def profile(request):
    person = request.session.get('cuser')
    data = signuptbl.objects.all().filter(email=person)
    return render(request,'profile.html',{'person':person, 'data':data})

def about(request):
    person = request.session.get('cuser')
    return render(request,'about.html',{'person':person})

def otp(request):
    timer = ""
    msg = ""
    if request.method == 'POST':
        if request.POST['otp'] == str(otp):
            print("Done")
            newreq.save()
            return redirect('Login')
        else:
            print("Error")
            msg = "Error!Invalid OTP"
    return render(request,'otp.html',{'msg':msg,'timer':timer})

def edituser(request):
    msg = ""
    person = request.session.get('cuser')
    cuser = signuptbl.objects.get(email = person)
    if request.method=='POST':
        updateReq = updateform(request.POST,instance=cuser)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('/')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!"
    return render(request,'edituser.html',{'person': person,'msg':msg,'cuser':cuser})

def node(request):
    person = request.session.get('cuser')
    if request.method == 'POST':
        newreq = notesForm(request.POST,request.FILES)
        if newreq.is_valid():
            newreq.save()
        else:
            print(newreq.errors)
    return render(request,'node.html',{'person':person})