from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def home(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = TodoItem(text=form.cleaned_data['text'])
            todo_item.save()
            return redirect('home')
    else:
        form = TodoItemForm()

    todo_items = TodoItem.objects.all()
    return render(request, 'home.html', {'todo_items': todo_items, 'form': form})
