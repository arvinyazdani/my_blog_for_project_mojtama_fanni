from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

#model profile for user
class Profile(models.Model):

    GENER_CHOICES = (("men","Men"),("women","Women"))
    WRITOR_CHOICES = (("writer","Writer"),("reader","Reader"))
  
    user = models.OneToOneField(User ,\
        on_delete=models.CASCADE, primary_key=True) 
    created_at = models.DateField(auto_now_add=True)
    sen = models.SmallIntegerField()
    id_number = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    bio = models.TextField(blank=True)
    gener = models.CharField(max_length=10, choices=GENER_CHOICES)
    is_writor = models.CharField(max_length=10, choices=WRITOR_CHOICES,\
         default="reader")
    file_resome = models.FileField(upload_to="users/files", blank=True,null=True) 

    
