from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
def upload_status_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.name,filename=filename)
class Status(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    content =models.TextField(null=True,blank=True)
    image   =models.ImageField(upload_to=upload_status_image,null=True,blank=True)
    timestamp =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.content)
    class Meta:
        verbose_name='status_post'
        verbose_name_plural='status posts'