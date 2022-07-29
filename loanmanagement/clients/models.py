
from django.db import models

GENDER_CHOICES = (
    
    ("Male", "Male"),
    ("Female", "Female"),
    
)


# Create your models here.
class Customer(models.Model):
  name=models.CharField(max_length=30)
  gender=models.CharField(max_length=40,choices=GENDER_CHOICES, default='Male')
  location=models.CharField(max_length=50)
  phone=models.IntegerField()

  def __str__(self):
    return self.name

  