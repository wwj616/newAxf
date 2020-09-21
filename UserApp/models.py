from django.db import models

# Create your models here.

class AxfUser(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=32)
    icon = models.ImageField(upload_to='icons')
    active = models.BooleanField(default=False)

    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'axf_user'
