from django.db import models
from Accounts.models import User


# Album model
class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='userrelalbum')
    name = models.CharField(max_length=200, verbose_name='نام آلبوم')
    date_created = models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_public = models.BooleanField(verbose_name='عمومی/خصوصی', default=False)
    download_count = models.IntegerField(default=0,verbose_name='تعداد دانلود')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'البوم ها'
        verbose_name = 'البوم'


class RequestJoin(models.Model):
    request_from = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربردرخواست دهنده',
                                     related_name='userrequestfrom')
    request_to = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربرپذیرنده',
                                   related_name='userrequestto')
    date_created = models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_accept = models.DateField(blank=True, null=True, verbose_name='تاریخ پذیرش')
    status = models.IntegerField(verbose_name='وضعیت درخواست', default=0)
    album_key = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_request', verbose_name='البوم')

    def __str__(self):
        return f"{self.request_to.username}---{self.request_from.username}"

    class Meta:
        verbose_name_plural = 'درخواست های شراکت'
        verbose_name = 'درخواست شراکت'


class MembersAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='عضو', related_name='memberrelalbum')
    album_key = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_member', verbose_name='البوم')
    admin = models.BooleanField(default=False, verbose_name='ادمین/عادی')

    def __str__(self):
        return f"{self.user.username}---{self.album_key.name}"

    class Meta:
        verbose_name_plural = 'اعضای البوم ها'
        verbose_name = 'اعضای البوم'


def uploadmodel_file_upload_to(instance, filename):
    return 'uploads/%s/%s' % (instance.user.username, filename)


class UploadModel(models.Model):
    file_name = models.CharField(max_length=200, blank=True, default='', verbose_name='نام فایل')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='کاربر',
                             related_name='upload_album')
    file = models.FileField(upload_to=uploadmodel_file_upload_to)
    type_file = models.IntegerField(default=0, verbose_name='نوع فایل')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='البوم', related_name='file_album')
    public_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='لینک عمومی')
    private_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='لینک خصوصی')

    def __str__(self):
        return f"{self.user.username}---{self.file_name}"

    class Meta:
        verbose_name_plural = 'فایل های اپلودی'
        verbose_name = 'فایل آپلودی'
