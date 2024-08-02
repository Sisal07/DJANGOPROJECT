from django.db import models

# Create your models here.
class Venue(models.Model):
    image=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    capacity=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Online(models.Model):
    cus_name= models.CharField(max_length=50)
    cus_ph= models.CharField(max_length=14)
    email= models.EmailField()
    address=models.CharField(max_length=50)
    datetime= models.DateTimeField()
    booked_on= models.DateTimeField(auto_now=True)
    name= models.ForeignKey(Venue, on_delete=models.CASCADE)
    type= models.CharField(max_length=50)
    guest= models.CharField(max_length=50)
    budget= models.CharField(max_length=50)
    service= models.CharField(max_length=100)
    request= models.TextField(max_length=300)
    def __str__(self):
        return f'{self.cus_name} - {self.cus_ph}'
    
class Contact(models.Model):
    c_name= models.CharField(max_length=50)
    c_email= models.EmailField()
    subject= models.CharField(max_length=100)
    message= models.TextField(max_length=300)
    def __str__(self):
        return f'{self.c_name} - {self.subject}'


