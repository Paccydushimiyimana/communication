from django.db import models
from account.models import MyUser
from django.urls import reverse

class Announce(models.Model):
    title=models.CharField(max_length=100, unique=True)
    content=models.TextField(max_length=1000)
    sender=models.ForeignKey(MyUser,related_name='+',on_delete=models.SET_NULL,null=True)
    receiver=models.ManyToManyField(MyUser, related_name='+',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    view_by=models.ManyToManyField(MyUser,related_name='+',blank=True)

    def __str__(self):
        return self.title
  

