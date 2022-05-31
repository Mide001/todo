from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import todo_now
# Create your views here.
def todo_add(request):
    form=todo_now.objects.all()
    form=TodoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('todo')
    else:
        form=TodoForm()
    form=todo_now.objects.all()
    return render(request, 'todo.html', {'form':form})

def delete(request,id):
    item=todo_now.objects.get(id=id)
    items=item.delete()
    return redirect('todo')