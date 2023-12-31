# Generated by Django 4.1.3 on 2023-10-20 07:05

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fname', models.CharField(max_length=100, verbose_name='نام')),
                ('lname', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='نام کاربری')),
                ('email', models.CharField(max_length=200, verbose_name='ایمیل')),
                ('re_email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل جایگزین')),
                ('password', models.CharField(max_length=200, verbose_name='رمز')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('profile', models.ImageField(blank=True, default='user', upload_to='profiles', verbose_name='عکس کاربر')),
                ('bio', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
