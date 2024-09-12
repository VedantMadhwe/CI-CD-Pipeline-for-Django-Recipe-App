from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    # agar woh reference table jaha pe ye model added hai woh delete hojata hai toh... (cascade hai toh... set_null hai toh....)
    #models.CASCADE : agar woh user delete hota hai toh usse related saari recipes delete kardo
    #models.SET_NULL : agar woh user delete hota hai toh usne recipes jo create kiye hai woh saaro pe null lag jaayga   
    # models.SET_DEFAULT : agar woh user delete hota hai toh uske jagah ek defalut value ko set karte hai

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField(default='default description')
    recipe_image=models.ImageField(upload_to="recipe")
    recipe_view_count = models.IntegerField(default = 1)


    class Meta:
        db_table="vege_recipe" 

class Department(models.Model):
    department = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']
    
class StudentID(models.Model):
    student_id = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name = "depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField(unique = True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"