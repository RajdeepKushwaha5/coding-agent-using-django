from django import forms

class TodoItemForm(forms.Form):
    text = forms.CharField(label='Todo', max_length=200, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
