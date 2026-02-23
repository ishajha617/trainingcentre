from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})


def enroll(request):

    courses = Course.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course_id = request.POST.get('course')

        course = get_object_or_404(Course, id=course_id)

        Enrollment.objects.create(
            student_name=name,
            email=email,
            phone=phone,
            course=course
        )

        return redirect('/')

    return render(request, 'enroll.html', {'courses': courses})