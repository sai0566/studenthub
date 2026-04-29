from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()


def create_demo_users():
    if not User.objects.filter(username='admin1').exists():
        User.objects.create_superuser(
            username='admin1',
            email='admin1@gmail.com',
            password='admin123',
            role='admin'
        )

    if not User.objects.filter(username='teacher1').exists():
        User.objects.create_user(
            username='teacher1',
            email='teacher1@gmail.com',
            password='teacher123',
            role='teacher'
        )

    if not User.objects.filter(username='student1').exists():
        User.objects.create_user(
            username='student1',
            email='student1@gmail.com',
            password='student123',
            role='student'
        )


def login_view(request):
    create_demo_users()

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