from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm, TaskForm
from .models import Tasks

# Create your views here.

def loginPage(request):

    form = SignupForm()

    if request.method == 'POST':
        if request.POST.get('submit') == 'Login':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, "Invalid Username!!")
                return redirect('home')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, "Invalid Username or Password!!")

        elif request.POST.get('submit') == 'Signup':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Password can’t be too similar to your other personal information.")
                messages.error(request, "Password must contain at least 8 characters.")
                messages.error(request, "Password can’t be a commonly used password.")
                messages.error(request, "Password can’t be entirely numeric.")
                return redirect('home')


    context = {'form': form}
    return render(request, 'base/login.html', context)

# ---------------LOGOUT PAGE------------------

@login_required
def logoutPage(request):
    logout(request)
    return redirect('home')

# ---------------HOME PAGE------------------

@login_required
def homePage(request):
    tasks = Tasks.objects.filter(user=request.user)

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
        return redirect('home')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

# ---------------EDIT TASK PAGE------------------

@login_required
def editTask(request, pk):
    task = Tasks.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form, 'task': task}
    return render(request, 'base/edit-task.html', context)

# ---------------DELETE TASK PAGE------------------

@login_required
def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'base/delete-task.html', context)
