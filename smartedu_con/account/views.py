from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from courses.models import Course
from . forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Disabled Account')
            else:
                messages.info(request, 'Invalid Username or Password')
    else:
        form = LoginForm()

    return render(request, 'account/Login.html', {'form': form})


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('Login')

    else:
        form = RegisterForm()

    return render(request, 'account/Register.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='Login')
def Dashboard(request):
    currentUser = request.user

    courses = currentUser.courses_joined.all()

    context = {
        'courses': courses,
    }

    return render(request, 'account/dashboard.html', context)


def enroll_the_course(request):
    course_id = request.POST['course_id']
    user_id = request.POST['user_id']
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=user_id)
    course.student.add(user)

    return redirect('Dashboard')


def release_the_course(request):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    course.student.remove(user)

    return redirect('Dashboard')
