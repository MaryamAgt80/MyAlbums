from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fname = models.CharField(max_length=100, verbose_name='نام')
    lname = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    username = models.CharField(max_length=200, unique=True, verbose_name='نام کاربری')
    email = models.CharField(max_length=200, verbose_name='ایمیل')
    re_email = models.CharField(max_length=200, blank=True, null=True, verbose_name='ایمیل جایگزین')
    password = models.CharField(max_length=200, verbose_name='رمز')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    profile = models.ImageField(upload_to='profiles',null=True, default='user.jpg', blank=True, verbose_name='عکس کاربر')
    bio = models.CharField(max_length=300, blank=True, null=True, default='')
    code=models.CharField(max_length=100,null=True,blank=True,default='',verbose_name='کد فعالسازی')
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'


