from django.shortcuts import render
from django.utils.translation.template import context_re

from main.models import Student


# Create your views here.
def index(request):
    students_list = Student.objects.all()
    context = {
        'objects_list': students_list,
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)

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