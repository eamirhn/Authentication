from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User ,AbstractBaseUser
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.reverse_related import ManyToManyRel


class Medicine(models.Model):
    medicineID = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=45,null = False)
    def __str__(self):
        return self.name


class Therapy_List(models.Model):
    therapy_listID = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=45,null = False)
    def __str__(self):
        return self.name


    Medicine_IDmedicine = models.ForeignKey(
    Medicine, on_delete=models.CASCADE, blank=True, null=False)
    Dosage = models.CharField(max_length=45,null=False)

class Therapy(models.Model):
    therapyID = models.IntegerField(primary_key=True,null=False)
    
    #ForigenKey
    User_IDpatient = models.ForeignKey(
    User, on_delete=models.CASCADE, blank=True, null=False)
    User_IDmed = models.IntegerField(null=True)
    TherapyList_IDtherapylist = models.ForeignKey(
    Therapy_List, on_delete=models.CASCADE, blank=True, null=False)



class Test(models.Model):
    testID = models.IntegerField(primary_key=True,null=False)
    dateTime = models.DateTimeField(null=False)

    #ForigenKey
    Therapy_IDtherapy = models.ForeignKey(
    Therapy, on_delete=models.CASCADE, blank=True, null=False)



class Test_Session(models.Model):
    test_SessionID = models.IntegerField(primary_key=True,null=False)
    test_type = models.IntegerField(null=False)
    DataURL = models.CharField(max_length=255,null = False)

    #ForigenKey
    Test_IDtest = models.ForeignKey(
    Test, on_delete=models.CASCADE, blank=True, null=False)
    def __str__(self):
        return self.DataURL


class Note(models.Model):
    noteID = models.IntegerField(primary_key=True,null=False)
    note = models.TextField()

    #ForigenKey
    Test_Session_IDtest_session = models.ForeignKey(
    Test_Session, on_delete=models.CASCADE, blank=True, null=False)
    User_IDmed = models.ForeignKey(
    User, on_delete=models.CASCADE, blank=True, null=False)
    def __str__(self):
        return self.note






class Organization(models.Model):
    organizationID = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=255,null = False)
    def __str__(self):
        return self.name

class Role(models.Model):
    roleID = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=45,null = False)
    type = models.CharField(max_length=45,null = False)
    def __str__(self):
        return self.name


class User(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    userID = models.IntegerField(primary_key=True,null=False)
    Role_IDrole = models.ForeignKey(
        Role, on_delete=models.CASCADE,null=False)
    Organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=False)
    

    email = models.EmailField(max_length=255)
    lat = models.FloatField(default=None,null=True,blank=True)
    long = models.FloatField(default=None,null=True,blank=True)

    provider = models.CharField(max_length=20,null=True,blank=True)



class Comments(models.Model):
    data_id = models.IntegerField(null=True,blank=True)
    user = models.CharField(max_length=40,null=True,blank=True)
    comment = models.TextField()
    dateAdded = models.DateTimeField(auto_now=True,null=True,blank=True)
