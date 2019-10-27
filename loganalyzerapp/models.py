from django.db import models

# Create your models here.
class log(models.Model):
    file=models.FileField(null=True)
    file_path = models.CharField(max_length=255,null=True)


class log_fields(models.Model):
    lp_adrees     =models.CharField(max_length=20)
    date_time     =models.CharField(max_length=50)
    res_code      =models.IntegerField()
    memory         =models.IntegerField()
    url_loction   =models.CharField(max_length=500)
    method        =models.CharField(max_length=10)



