# Generated by Django 4.1.3 on 2023-10-22 15:56

import Album.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام آلبوم')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('is_public', models.BooleanField(default=False, verbose_name='عمومی/خصوصی')),
                ('download_count', models.IntegerField(verbose_name='تعداد دانلود')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrelalbum', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'البوم',
                'verbose_name_plural': 'البوم ها',
            },
        ),
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, default='', max_length=200, verbose_name='نام فایل')),
                ('file', models.FileField(upload_to=Album.models.uploadmodel_file_upload_to)),
                ('type_file', models.IntegerField(default=0, verbose_name='نوع فایل')),
                ('public_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک عمومی')),
                ('private_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک خصوصی')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_album', to='Album.album', verbose_name='البوم')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='upload_album', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'فایل آپلودی',
                'verbose_name_plural': 'فایل های اپلودی',
            },
        ),
        migrations.CreateModel(
            name='RequestJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_accept', models.DateField(blank=True, null=True, verbose_name='تاریخ پذیرش')),
                ('status', models.IntegerField(default=0, verbose_name='وضعیت درخواست')),
                ('album_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_request', to='Album.album', verbose_name='البوم')),
                ('request_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequestfrom', to=settings.AUTH_USER_MODEL, verbose_name='کاربردرخواست دهنده')),
                ('request_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequestto', to=settings.AUTH_USER_MODEL, verbose_name='کاربرپذیرنده')),
            ],
            options={
                'verbose_name': 'درخواست شراکت',
                'verbose_name_plural': 'درخواست های شراکت',
            },
        ),
        migrations.CreateModel(
            name='MembersAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False, verbose_name='ادمین/عادی')),
                ('album_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_member', to='Album.album', verbose_name='البوم')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberrelalbum', to=settings.AUTH_USER_MODEL, verbose_name='عضو')),
            ],
            options={
                'verbose_name': 'اعضای البوم',
                'verbose_name_plural': 'اعضای البوم ها',
            },
        ),
    ]
