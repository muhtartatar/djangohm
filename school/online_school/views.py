from django.shortcuts import render, redirect
from .models import User


def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        language = request.POST.get('language')
        user = User(name=name, language=language)
        user.save()
        return redirect('choose_course')
    return render(request, 'add_user.html')


def choose_course(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        user = User.objects.latest('id')
        user.course = course
        user.save()
        return redirect('add_grade')
    return render(request, 'choose_course.html')


def add_grade(request):
    user = User.objects.latest('id')
    user.save()
    return redirect('students_list')


def students_list(request):
    users = User.objects.all()
    return render(request, 'students_list.html', {'users': users})
