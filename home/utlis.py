# it uses some of the Django system things lets say models
from .models import Student
import time

def run_this_function():
    print("Function Started")
    time.sleep(1)
    print("Function executed.")