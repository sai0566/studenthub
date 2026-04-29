from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from students.models import Student
from students.forms import StudentForm

# Utility function (Optional: you can also use custom decorators)
def teacher_required(user):
    return user.is_authenticated and user.role == 'teacher'


@login_required
def teacher_students(request):
    # Security check
    if request.user.role != 'teacher':
        return redirect('dashboard')

    # Fetch only students assigned to this teacher, ordered by newest
    students = Student.objects.filter(assigned_teacher=request.user).order_by('-id')
    query = request.GET.get('q')

    # Apply Search Logic
    if query:
        students = students.filter(
            Q(user__username__icontains=query) |
            Q(roll_number__icontains=query) |
            Q(class_name__icontains=query)
        )

    # Apply Pagination Logic (10 students per page)
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page', 1)

    try:
        paginated_students = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_students = paginator.page(1)
    except EmptyPage:
        paginated_students = paginator.page(paginator.num_pages)

    # Make sure 'my_students.html' matches whatever you named your list template!
    return render(request, 'teacher_students.html', {'students': paginated_students})


@login_required
def edit_student(request, pk):
    if request.user.role != 'teacher':
        return redirect('dashboard')

    student = get_object_or_404(Student, id=pk, assigned_teacher=request.user)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('teacher_students') # Make sure this matches your urls.py name

    return render(request, 'student_form.html', {'form': form, 'title': 'Edit Student', 'student': student})


@login_required
def delete_student(request, pk):
    if request.user.role != 'teacher':
        return redirect('dashboard')

    student = get_object_or_404(Student, id=pk, assigned_teacher=request.user)

    if request.method == 'POST':
        student.delete()
        return redirect('teacher_students')

    return render(request, 'delete_student.html', {'student': student})