from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from datetime import date
from students.models import Student
from .models import Attendance


@login_required
def mark_attendance(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')

    students = Student.objects.filter(assigned_teacher=request.user)

    if request.method == 'POST':
        attendance_date = request.POST.get('date')

        for student in students:
            status = request.POST.get(f'status_{student.id}')

            if status:
                Attendance.objects.update_or_create(
                    student=student,
                    date=attendance_date,
                    defaults={'status': status}
                )

        return redirect('dashboard')

    return render(request, 'mark_attendance.html', {
        'students': students,
        'today': date.today()
    })



from django.db.models import Count, Q
from students.models import Student
from .models import Attendance
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def student_attendance(request):
    if request.user.role != 'student':
        return redirect('dashboard')

    student = Student.objects.get(user=request.user)

    records = Attendance.objects.filter(student=student).order_by('-date')

    total_days = records.count()
    present_days = records.filter(status='present').count()

    percentage = 0
    if total_days > 0:
        percentage = (present_days / total_days) * 100

    return render(request, 'student_attendance.html', {
        'records': records,
        'total_days': total_days,
        'present_days': present_days,
        'percentage': round(percentage, 2)
    })