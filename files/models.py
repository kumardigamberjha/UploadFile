from django.db import models

class UplaodFile(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    adhar = models.CharField(max_length=16)
    datentime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name