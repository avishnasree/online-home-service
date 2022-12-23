from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)


class addworkermanagement(models.Model):
    name=models.CharField(max_length=100)
    charge=models.IntegerField()
    discription=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class userpage(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='users')
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    housenumber=models.IntegerField(max_length=10)
    phonenumber=models.IntegerField(max_length=15)
    email=models.EmailField()
    photo=models.ImageField(upload_to='photo')

    def __str__(self):
        return self.name




class workerpage(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='worker')
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    phonenumber=models.IntegerField(max_length=20)
    worketype=models.ForeignKey(addworkermanagement,on_delete=models.CASCADE)
    workerid=models.IntegerField(max_length=30)
    photo=models.ImageField(upload_to='photo')
    email=models.EmailField()

    def __str__(self):
        return self.name


class workershedule(models.Model):
    employee=models.ForeignKey(workerpage,on_delete=models.CASCADE)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()





class addappoinment(models.Model):
    user=models.ForeignKey(userpage,on_delete=models.CASCADE,related_name='appointment')
    schedule=models.ForeignKey(workershedule,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)


class addfeedback(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date=models.DateField()
    time=models.TimeField()
    feedback=models.CharField(max_length=1000)
    reply=models.TextField(null=True, blank=True)

class payment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    payment=models.IntegerField(default=0)



class add_payment(models.Model):
    user = models.ForeignKey(userpage,on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    bill_date = models.DateField(auto_now=True)
    paid_on = models.DateField(auto_now=True)
    status=models.IntegerField(default=0)













