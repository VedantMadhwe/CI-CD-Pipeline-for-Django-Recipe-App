from django.db import models

# Create your models here.

class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    # agar name 100 se bada hoga toh error
    age = models.IntegerField()
    # IntegerField(default=18) rehta hai
    email=models.EmailField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    image=models.ImageField()
    file=models.FileField()
    # field=models.DateTimeField()

# class Product(models.Model):
#     pass

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
    # ye 
    # <QuerySet [<Car: Car object (1)>, <Car: Car object (2)>, <Car: Car object (3)>, <Car: Car object (4)>, <Car: Car object (5)>, <Car: Car object (6)>, <Car: Car object (7)>]>
    #  aise car object ke format ko readable form me laane ke liye upar ka 'double str' vala function use kiya hai