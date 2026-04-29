from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from students.models import Student
from .models import Result
from .forms import ResultForm


@login_required
def add_result(request, student_id):
    if request.user.role != 'teacher':
        return redirect('dashboard')

    student = get_object_or_404(
        Student,
        id=student_id,
        assigned_teacher=request.user
    )

    form = ResultForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            subject = form.cleaned_data['subject']
            marks = form.cleaned_data['marks']
            total_marks = form.cleaned_data['total_marks']

            Result.objects.update_or_create(
                student=student,
                subject=subject,
                defaults={
                    'marks': marks,
                    'total_marks': total_marks
                }
            )

            messages.success(request, 'Marks saved successfully.')
            return redirect('teacher_students')

    return render(request, 'add_result.html', {
        'form': form,
        'student': student
    })


@login_required
def student_results(request):
    if request.user.role != 'student':
        return redirect('dashboard')

    student = get_object_or_404(Student, user=request.user)
    results = Result.objects.filter(student=student)

    total_obtained = sum(result.marks for result in results)
    total_possible = sum(result.total_marks for result in results)

    percentage = 0
    if total_possible > 0:
        percentage = (total_obtained / total_possible) * 100

    if not results.exists():
        overall_status = "No Results"
    elif results.filter(marks__lt=35).exists():
        overall_status = "Fail"
    else:
        overall_status = "Pass"

    return render(request, 'student_results.html', {
        'results': results,
        'total_obtained': total_obtained,
        'total_possible': total_possible,
        'percentage': round(percentage, 2),
        'overall_status': overall_status
    })