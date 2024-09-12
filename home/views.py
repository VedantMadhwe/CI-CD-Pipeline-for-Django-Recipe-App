from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # creating a list
    peoples = [
        {'name': 'Vedant Madhwe', 'age':20},
        {'name': 'Aditya Madhwe', 'age':14},
        {'name': 'Virat Kohli', 'age':26},
        {'name': 'Sachin Tendulakr', 'age':40},
        {'name': 'MS Dhoni', 'age':39}
        
    ]
    
    vegetables =['pumpkins', 'Tomato', 'Cucumber']


    return render(request, "home/index.html", context = {'page' : 'Django Learning','peoples' : peoples})



def success_page(request):
    print("*" *10)
    return HttpResponse("""<h2>Hey this is a success page...</h2>""")

def contact(request):
    context = {'page': 'Contact'}
    return render(request,"home/contact.html", context)

def about(request):
    context = {'page': 'About'}
    return render(request,"home/about.html", context)