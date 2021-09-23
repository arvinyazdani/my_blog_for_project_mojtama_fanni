from typing import NewType
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProfileUserFrom
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method != "POST":   
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blog:post_list')
    context = {"form":form}
    return render(request, "registration/register.html", context)
@login_required
def profile_register(request,user_id):
    user = User.objects.get(id=user_id)
    if request.method != "POST":   
        form = ProfileUserFrom()
    else:
        form = ProfileUserFrom(data=request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = user
            new_profile.save()
            return redirect('users:profile',user_id=user_id)
    context = {"form":form,"user_id":user_id}
    return render(request, "registration/register_profile.html", context)
'''
def register_full(request,user_id=None,step=None):
    if request.method != "POST":   
        form = UserCreationForm()
        step = 1
    else:
        if step == 1:    
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                user_id = new_user.id
                user = User.objects.filter(id=user_id)
                form = ProfileUserFrom()
                step = 2
                context = {
                    "form":form, 'step':step, "user":user
                    }        
                return (request,"registration/register_profile.html",context)
        elif step == 2:
            form = ProfileUserFrom(data=request.POST)
            if form.is_valid():
                user = User.objects.filter(id=user_id)
                new_profile = form.save(commit=False)
                new_profile.user = user
                new_profile.save()
                login(request, user)
                return redirect('blog:post_list')
    context = {
        "form":form, 'step':step
    }        
    return render(request, "registration/register_profile.html", context)

#aval user register shavad badesh profile

'''
@login_required
def profile(request,user_id):
    user = User.objects.get(id=user_id)
    try:
        profile = user.profile
    except ObjectDoesNotExist:
        return redirect("users:register_profile", user_id=user_id)    
    context = {"user":user,"profile":profile}
    return render(request, "profile.html", context)
@login_required
def edite_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = user.profile
    if request.user != user:raise Http404
    if request.method != "POST":form = ProfileUserFrom(instance=profile)  
    else:
        form = ProfileUserFrom(instance=profile,  data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('users:profile', user_id=user_id) 
    context = {"form":form, 'user':user}
    return render(request, "registration/edite_profile.html", context)        
    
