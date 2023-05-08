from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def main(request):
    return render(request, 'main.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['pass_word']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('courseapp/add/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['pass_word']
        cpassword = request.POST['pass_word1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')

            user = User.objects.create_user(username=username, password=password)

            user.save()
            return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
