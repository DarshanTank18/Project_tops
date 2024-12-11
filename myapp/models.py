from django.db import models

# Create your models here.

class signuptbl(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    fnm = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.BigIntegerField()
    password = models.CharField(max_length=10)

class nodetbl(models.Model):
    quert_title = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    node_image = models.FileField(upload_to='query_images')
    node_desc = models.CharField(max_length=10)

class contectustbl(models.Model):
    uname = models.CharField(max_length=20)
    mail = models.EmailField()
    message = models.CharField(max_length=200)