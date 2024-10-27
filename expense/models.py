from django.db import models
from tokenize import group 
# from django.contrib.auth.models import AbstractUser

# for user login and signup model 
class Login_or_Signup (models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=200)
    phone_number = models.CharField(max_length=150) 
# to return the name and pw of login or signup user in the disply

    def __str__(self):
        return self.name
#to display the group of models
class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_status = models.CharField(max_length=20,default='pending')
    date = models.DateTimeField()
    def __str__(self):
        return self.group_name
class Group_membership(models.Model):
    user_id = models.ForeignKey(Login_or_Signup,on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user_id}-{self.group_id}"
    
class Bill_detail(models.Model):
    bill_name = models.CharField(max_length=100,default='bill-name')
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE,default=None)
    amount = models.FloatField()
    # split_type here means the ways in which amount dividing among member assosiated with group id 
    split_type = models.CharField(max_length=50,default='EQUAL')
    date = models.DateTimeField()
    status = models.CharField(max_length=20,default="pending")
    def __str__(self):
        return f"{self.bill_name}-{self.group_id}-{self.amount}-{self.status}"
class Friend(models.Model):
    user_id = models.ForeignKey(Login_or_Signup,on_delete=models.CASCADE,related_name='friends')
    friend_id = models.ForeignKey(Login_or_Signup,related_name="friend",on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=50,default='pending')
    def __str__(self):
        return f"{self.user_id}-{self.friend_id}-{self.group_id}-{self.status}"
    
class Vender(models.Model):
    name = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    contact_number = models.CharField(max_length=255,blank=True)
    email =models.EmailField(blank=True,null=True)
    website = models.URLField(blank=True)
    def __str__(self):
        return self.name # just return vender name

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateTimeField()
    user_id = models.ForeignKey(Login_or_Signup, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vender, on_delete=models.CASCADE)  # Ensure this field exists
    split_type = models.CharField(max_length=50, default='EQUAL')  # Ensure this field exists
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.title} - {self.amount} - {self.date}"

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # Content of the note
    created_by = models.ForeignKey(Login_or_Signup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.created_by} - {self.created_at}"