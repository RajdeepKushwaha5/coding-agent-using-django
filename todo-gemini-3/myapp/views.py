from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
        return redirect('home')
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})