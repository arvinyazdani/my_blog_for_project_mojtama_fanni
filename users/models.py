from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

#model profile for user
class Profile(models.Model):

    GENER_CHOICES = (("men","Men"),("women","Women"))
    WRITOR_CHOICES = (("writer","Writer"),("reader","Reader"))
  
    user = models.OneToOneField(User ,\
        on_delete=models.CASCADE, primary_key=True\
            , verbose_name="کاربر") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایحاد", null=True, blank=True)
    sen = models.SmallIntegerField( verbose_name="سن")
    id_number = models.CharField(max_length=10, verbose_name="شماره ملی")
    phone = models.CharField(max_length=11, verbose_name="تماس")
    bio = models.TextField(blank=True, verbose_name="بیو")
    gener = models.CharField(max_length=10, choices=GENER_CHOICES, verbose_name="جنسیت")
    is_writor = models.CharField(max_length=10, choices=WRITOR_CHOICES,\
         default="reader", verbose_name="ایا نویسنده")
    file_resome = models.FileField(upload_to="users/files", blank=True,null=True, verbose_name="فایل رزومه") 

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'



    
