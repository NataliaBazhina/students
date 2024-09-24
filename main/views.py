from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation.template import context_re
from django.views.generic import ListView, DetailView, CreateView

from main.models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}) : {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)

class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy("main:index")