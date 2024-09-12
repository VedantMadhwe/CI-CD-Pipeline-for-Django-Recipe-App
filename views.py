from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        
        # print("recipe name = ", recipe_image)
        # print("recipe Description = ",recipe_name)
        # print("recipe Image = ",recipe_desciption)
        
        Recipe.objects.create(
            recipe_image= recipe_image,
            recipe_name= recipe_name,
            recipe_description= recipe_description,
            )
        return redirect('/recipes/')
    

    queryset = Recipe.objects.all()

    # search vala code 
    if request.GET.get('search'):
        # print(request.GET.get('search')) #Output pudding
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
        # queryset = queryset.filter(recipe_description__icontains = request.GET.get('search'))
    
    # if request.GET.get('search'):
    #     # print(request.GET.get('search')) #Output pudding
    #     # queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    #     queryset = queryset.filter(recipe_description__icontains = request.GET.get('search'))
    

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)

def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/') 

def update_recipe(request, id):
    
    queryset = Recipe.objects.get(id = id)
    

    if request.method == "POST":
        data = request.POST

        recipe_name= data.get('recipe_name')
        recipe_description= data.get('recipe_description')
        recipe_image= request.FILES.get('recipe_image')
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')


    context = {'recipe' : queryset}
    return render(request,'update_recipes.html', context) 

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

# filter the user agar woh already exist karta hai ki nhi
# if it exists => true , else => false
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')

        # this helps in remaining logged in, in the session.
        else:
            login(request, user)
            return redirect('/recipes/')


    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # special method is called to encrypt the password in django automatically

        user = User.objects.filter(username = username)

        if user.exists():
            # messages ko flash karva rahe hai taaki user ko pata chale that username pehle hi use ho chuka hai
            messages.error(request,'Username Already taken')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,

        )
        
        user.set_password(password)
        user.save()
        messages.success(request,'Account created successfully')

        return redirect('/register/')

    return render(request,'register.html')

# username = vedant_1
# password = 123