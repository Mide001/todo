from .models import todo_now
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_now
        fields = ['title', 'content']