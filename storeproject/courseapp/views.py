from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentCreationForm
from .models import Student, Course


from django.contrib import messages

def student_create_view(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order has been placed successfully!')
            return redirect('student_add')
    return render(request, 'courseapp/home.html', {'form': form})


def student_update_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentCreationForm(instance=student)
    if request.method == 'POST':
        form = StudentCreationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_change', pk=pk)
    return render(request, 'courseapp/home.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'courseapp/course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(courses.values('id', 'name')), safe=False)



