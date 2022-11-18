from django.db import models

# Create your models here.
class EmployeeDatabase(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Firstname
   
    class Meta:
        verbose_name_plural="EmployeeDB"