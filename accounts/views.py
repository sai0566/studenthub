from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return render(request, 'admin_dashboard.html')

    elif request.user.role == 'teacher':
        return render(request, 'teacher_dashboard.html')

    elif request.user.role == 'student':
        return render(request, 'student_dashboard.html')

    return redirect('login')
    


