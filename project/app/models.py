from django.db import models

# Create your models here.
class UserDatabase(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.fname
    
    class Meta:
        verbose_name_plural="UserDB"