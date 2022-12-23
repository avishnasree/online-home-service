from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.transaction import commit
from django.shortcuts import render, redirect


# Create your views here.
from homeserviceapp.forms import LoginRegister, userform, workerform, worksheduleform, addworksheduleform, \
    addappointmentform, addfeedbackform, add_paymentform
from homeserviceapp.models import workerpage, userpage, workershedule, addappoinment, addfeedback, addworkermanagement, \
    payment, add_payment


def mainpage(request):
    return render(request,'index2.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_user:
                return redirect('user')
            elif user.is_worker:
                return redirect('worker')
        else:
            messages.info(request,'invalid')
    return render(request,'loginpage.html')


def admin_page(request):
    return render(request,'adminpage.html')

def register(request):
    return render(request,'register.html')

def worker(request):
    return render(request,'worker.html')


def user(request):
    return render(request,'user.html')


def userregister(request):
    user_form=LoginRegister()
    userregister_form=userform()
    if request.method=='POST':
        user_form=LoginRegister(request.POST)
        userregister_form=userform(request.POST,request.FILES)
        if user_form.is_valid() and userregister_form.is_valid():
            user=user_form.save(commit=False)
            user.is_user=True
            user.save()
            userregister=userregister_form.save(commit=False)
            userregister.user=user
            userregister.save()
            messages.info(request,'Register Successfully')
            return redirect("login_page")
    return render(request,'userregister.html',{'user_form':user_form,'userregister_form':userregister_form})

def workerregister(request):
    user_form=LoginRegister()
    workerregister_form=workerform()
    if request.method=='POST':
        user_form=LoginRegister(request.POST)
        workerregister_form=workerform(request.POST,request.FILES)
        if user_form.is_valid() and workerregister_form.is_valid():
            user=user_form.save(commit=False)
            user.is_worker=True
            user.save()
            workerregister=workerregister_form.save(commit=False)
            workerregister.user=user
            workerregister.save()
            messages.info(request,'Register Successfully')
            return redirect("login_page")
    return render(request,'workerregister.html',{'worker_form':user_form,'workerregister_form':workerregister_form})

def viewuser(request):
    data=userpage.objects.all()
    return render(request,'viewuser.html',{'data':data})


def delete_user(request,id):
    userpage.objects.get(id=id).delete()
    return redirect('viewuser')


def viewworker(request):
    data=workerpage.objects.all()
    return render(request,'viewworker.html',{'data':data})

def delete_worker(request,id):
    data=workerpage.objects.get(id=id).delete()
    return redirect('viewworker')


def update_worker(request,id):
    data=workerpage.objects.get(id=id)
    form=workerform(instance=data)
    if request.method=='POST':
        form=workerform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewworker')
    return render(request,'updateworker.html',{'form':form})


def viewworkeruser(request):
    data = workerpage.objects.all()
    return render(request, 'viewworkeruser.html', {'data': data})


def sheduleview(request):
    data=workershedule.objects.all()
    return render(request,'shedule.html',{'data':data})


def addworkershedule(request):
    form=worksheduleform()
    if request.method=='POST':
        form=worksheduleform(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.employee=workerpage.objects.get(user=request.user)
            form.save()
            return redirect('sheduleview')
    return render(request,'addworkershedule.html',{'form':form})


def update_shedule(request,id):
    data=workershedule.objects.get(id=id)
    form=worksheduleform(instance=data)
    if request.method=='POST':
        form=worksheduleform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('sheduleview')
    return render(request,'updateshedule.html',{'form':form})


def delete_shedule(request,id):
    data=workershedule.objects.get(id=id).delete()
    return redirect('sheduleview')


def viewworkershedule(request):
    s = workershedule.objects.all()
    context={
        'schedule':s
    }
    return render(request, 'viewworkershedule.html',context)


def addworkmanagement(request):
    form=addworksheduleform
    if request.method=='POST':
        form=addworksheduleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewworkmanagement')
    return render(request,'addworkmanagement.html',{'form':form})


def viewworkmanagement(request):
    data = addworkermanagement.objects.all()
    return render(request, 'viewworkmanagement.html', {'data': data})



# def addappointment(request):
#     form=addappointmentform
#     if request.method=='POST':
#         form=addappointmentform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sheduleview')
#     return render(request,'add_appointment.html',{'form':form})


def viewappointment(request):
    data = addappoinment.objects.all()
    return render(request, 'viewappointment.html', {'data': data})


def addfeedbacks(request):
    form=addfeedbackform()
    u=request.user
    if request.method=='POST':
        form=addfeedbackform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('user')
    return render(request,'add_feedback.html',{'form':form})


def feedbackview(request):
    data=addfeedback.objects.filter(user=request.user)
    return render(request,'feedbackview.html',{'data':data})


def viewfeedbacks(request):
    data = addfeedback.objects.all()
    return render(request,'viewfeedback.html', {'data' : data})



def update_workmanagement(request,id):
    data=addworkermanagement.objects.get(id=id)
    form=addworksheduleform(instance=data)
    if request.method=='POST':
        form=addworksheduleform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewworkmanagement')
    return render(request,'update_workmanagement.html',{'form':form})


def delete_workmanagement(request,id):
    data=addworkermanagement.objects.get(id=id).delete()
    return redirect('viewworkmanagement')



def user_appointment(request,id):
    s=workershedule.objects.get(id=id)
    c=userpage.objects.get(user=request.user)
    appoinment = addappoinment.objects.filter(user=c,schedule=s)
    if appoinment.exists():
        messages.info(request,'You have already requested appointment for this schedule')
        return redirect('viewworkershedule')
    else:
        if request.method == 'POST':
            obj = addappoinment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appoinment booked successfully')
            return redirect('appointment_view')
    return render(request, 'add_appointment.html', {'schedule': s})


def appointment_view(request):
    c=userpage.objects.get(user=request.user)
    a=addappoinment.objects.filter(user=c)
    return render(request,'appointment_view.html',{'a':a})


def appointment_viewworker(request):
    a=addappoinment.objects.all()
    return render(request,'appointment_viewworker.html',{'a':a})


def appointment_viewadmin(request):
    a=addappoinment.objects.all()
    return render(request,'appointment_viewadmin.html',{'a':a})


def approve_appointment(request,id):
  a=addappoinment.objects.get(id=id)
  a.status=1
  a.save()
  messages.info(request,'Appoinment Confirmed')
  return redirect('appointment_viewadmin')



def reject_appointment(request,id):
    n=addappoinment.objects.get(id=id)
    n.status=2
    n.save()
    messages.info(request,'Appoinment Rejected')
    return redirect('appointment_viewadmin')




def admin_replay(request,id):
    f=addfeedback.objects.get(id=id)
    if request.method=='POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request,'Reply send for complaint')
        return redirect('admin_page')
    return render(request,'admin_replay.html',{'f':f})



def addpayments(request):
    form=add_paymentform()
    if request.method=='POST':
        form=add_paymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    return render(request,'addpayment.html',{'form':form})



def viewpayments(request):
    data=add_payment.objects.all()
    return render(request,'viewpayment.html',{'data':data})




def userpayment_view(request):
    c = userpage.objects.get(user=request.user)
    a = add_payment.objects.filter(user=c)
    return render(request,'userpayment_view.html',{'a':a})


def pay_now(request,id):
    n=add_payment.objects.get(id=id)
    n.status=0
    n.save()
    messages.info(request,'Appoinment Rejected')
    return redirect('userpayment_view')


def pay_direct(request,id):
    n=add_payment.objects.get(id=id)
    n.status=1
    n.save()
    messages.info(request,'Appoinment Rejected')
    return redirect('userpayment_view')


def pay_bttn(request):
    return render(request,'paynow_bttn.html')



def wrkr_paymentview(request):
    data=add_payment.objects.all()
    return render(request,'wrkr_paymentview.html',{'data':data})


def logout_view(request):
    logout(request)
    return redirect('login_page')
