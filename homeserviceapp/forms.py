from django import forms
from django.contrib.auth.forms import UserCreationForm

from homeserviceapp.models import userpage, workerpage, Login, workershedule, addworkermanagement, addappoinment, \
    addfeedback, payment, add_payment


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class userform(forms.ModelForm):
    class Meta:
        model=userpage
        exclude=('user',)


class workerform(forms.ModelForm):
    class Meta:
        model=workerpage
        exclude=('user',)

class worksheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time=forms.TimeField(widget=TimeInput)
    end_time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=workershedule
        exclude = ('employee',)



class addworksheduleform(forms.ModelForm):
    class Meta:
        model=addworkermanagement
        fields=('__all__')







class addappointmentform(forms.ModelForm):
    class Meta:
        model=addappoinment
        fields=('__all__')


class addfeedbackform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    class Meta:
        model=addfeedback
        exclude=('reply','user',)



class paymentform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    model=payment
    fields=('__all__')



class add_paymentform(forms.ModelForm):
    class Meta:
        model=add_payment
        exclude=('paid_on','bill_date','status',)

