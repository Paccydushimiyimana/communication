from django.db import models
from account.models import MyUser

class Announce(models.Model):
    title=models.CharField(max_length=100, unique=True)
    content=models.TextField(max_length=1000)
    creator=models.ForeignKey(MyUser,related_name='+',on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
