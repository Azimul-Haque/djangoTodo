from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # /task/71/
    url(r'^task/$', views.TaskList.as_view(), name='task_list'),

    # # task/create/
    url(r'task/create/$', views.TaskCreate.as_view(), name='task_create'),

    # # task/edit/71
    url(r'task/edit/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='task_edit'),

    # # task/delete/71
    url(r'task/delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='task_delete'),
]