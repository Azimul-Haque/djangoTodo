from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Task, Category, Priority
from django.contrib.auth.models import User


def index(request):
    return render(request, 'todo/index.html')

class TaskList(ListView):
    model = Task
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user.id, is_done=0)

class TaskCreate(SuccessMessageMixin, CreateView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = "Task created successfully!"
    fields = ['title', 'text', 'category', 'priority', 'is_pinned', 'is_done']
    exclude = ['created_by']

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = User.objects.get(id=self.request.user.id) # use your own profile here
        task.save()
        success_message = "Task created successfully!"
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect('/task/')

class TaskUpdate(SuccessMessageMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = "Task updated successfully!"
    fields = ['title', 'text', 'category', 'priority', 'is_pinned', 'is_done']
    exclude = ['created_by']

class TaskDelete(SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = "Task Deleted successfully!"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDelete, self).delete(request, *args, **kwargs)

class TaskDone(SuccessMessageMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = "Task is done!"
    fields = ['is_done']


