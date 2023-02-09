from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Husband(models.Model):
    name=models.CharField(max_length=100,null=True)
    religion=models.CharField(max_length=100,null=True)
    dob=models.DateField(max_length=100,null=True)
    marrital=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    zipcode=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    adhar=models.CharField(max_length=100,null=True)
    image=models.FileField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Wife(models.Model):
    name=models.CharField(max_length=100,null=True)
    religion=models.CharField(max_length=100,null=True)
    dob=models.DateField(max_length=100,null=True)
    marrital=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    zipcode=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    adhar=models.CharField(max_length=100,null=True)
    image=models.FileField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Witness(models.Model):
    name1=models.CharField(max_length=100,null=True)
    name2=models.CharField(max_length=100,null=True)
    name3=models.CharField(max_length=100,null=True)
    address1=models.CharField(max_length=100,null=True)
    address2=models.CharField(max_length=100,null=True)
    address3=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name1+" "+self.name2+" "+self.name3

class Status(models.Model):
    status = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.status

class Registration(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    report_status = models.CharField(max_length=100,null=True)
    u_id = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    husband = models.ForeignKey(Husband,on_delete=models.CASCADE,null=True)
    wife = models.ForeignKey(Wife,on_delete=models.CASCADE,null=True)
    witness = models.ForeignKey(Witness,on_delete=models.CASCADE,null=True)
    remark = models.CharField(max_length=100, null=True)
    marriage_date=models.DateField(null=True)
    reg_date=models.DateField(null=True)
    def __str__(self):
        return self.user.user.username+" "+self.husband.name+" "+self.wife.name

