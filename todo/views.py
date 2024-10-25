from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
	item_list = Todo.objects.order_by('-date')
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = TodoForm()
	page = {
		'forms': form,
		'list': item_list,
		'title': 'TODO_LIST',
	}
	return render(request, 'todo/index.html', page)


def remove(request, pk):
	item = Todo.objects.get(pk=pk)
	item.delete()
	messages.info(request, 'item removed!')
	return redirect('todo')